"""Maintainer-only: build native stages and capture real editor views.

Run with UnrealEditor -ExecutePythonScript. Captures use Slate ticks, not sleeps.
Output stays in this task's SMALL_WORLDS_EVIDENCE directory.
"""
from pathlib import Path
import json
import os
import sys
import time
import traceback
import unreal as ue

out = Path(os.environ['SMALL_WORLDS_EVIDENCE'])
out.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(Path(ue.Paths.project_dir()) / 'Content' / 'Python'))
import small_worlds as sw

results = []
for stage, map_name in [('starter', '01_PaperCity'), ('dusk', '02_Dusk'), ('festival', '03_LanternFestival'), ('cinematic', '04_Cinematic')]:
    if os.environ.get('SMALL_WORLDS_FROM_SAVED') == '1':
        sw.LEVELS.load_level(sw.ROOT + '/Maps/' + map_name)
        for actor in sw.ACTORS.get_all_level_actors():
            if actor.get_actor_label() == 'SW_FloatingSculpture':
                actor.static_mesh_component.set_static_mesh(sw.MESHES['Cube'])
            if actor.get_actor_label().startswith('SW_Roof_'):
                side = int(actor.get_actor_label().rsplit('_', 1)[1])
                actor.set_actor_rotation(ue.Rotator(-side * 30, 0, 0), False)
            if isinstance(actor, ue.PointLight):
                comp = actor.get_component_by_class(ue.PointLightComponent)
                festival_light = actor.get_actor_label().startswith('SW_FestivalLight_')
                comp.set_editor_property('intensity', 45.0 if festival_light else 90.0)
                comp.set_editor_property('light_color', ue.Color(r=255, g=137 if festival_light else 157, b=45 if festival_light else 67, a=255))
            if isinstance(actor, ue.DirectionalLight):
                comp = actor.get_component_by_class(ue.DirectionalLightComponent)
                comp.set_editor_property('light_color', ue.Color(r=235, g=243, b=255, a=255) if stage == 'starter' else ue.Color(r=255, g=181, b=119, a=255))
            if isinstance(actor, ue.PostProcessVolume):
                settings = actor.get_editor_property('settings')
                settings.set_editor_property('override_auto_exposure_apply_physical_camera_exposure', True)
                settings.set_editor_property('auto_exposure_apply_physical_camera_exposure', False)
                actor.set_editor_property('settings', settings)
            if isinstance(actor, ue.CineCameraActor):
                actor.get_cine_camera_component().set_editor_property('post_process_blend_weight', 0.0)
        sw.LEVELS.save_current_level()
        results.append(sw.verify(stage))
    else:
        results.append(sw.build(stage))
(out / 'build-results.json').write_text(json.dumps(results, indent=2))

jobs = [
    ('01_PaperCity', 'SW_Cam_Wide', '01-daylight.png'),
    ('02_Dusk', 'SW_Cam_Wide', '02-dusk.png'),
    ('03_LanternFestival', 'SW_Cam_Wide', '03-festival.png'),
    ('04_Cinematic', 'SW_Cam_Wide', '04-wide.png'),
    ('04_Cinematic', 'SW_Cam_Bridge', '05-bridge.png'),
    ('04_Cinematic', 'SW_Cam_Sculpture', '06-sculpture.png'),
]
state = {'index': 0, 'phase': 'load', 'at': time.monotonic(), 'busy': False, 'handle': None}
ue.EditorPythonScripting.set_keep_python_script_alive(True)


def finish(ok):
    ue.unregister_slate_post_tick_callback(state['handle'])
    (out / 'capture-result.json').write_text(json.dumps({'passed': ok, 'files': [j[2] for j in jobs], 'engine': ue.SystemLibrary.get_engine_version()}, indent=2))
    ue.log('SMALL_WORLDS_CAPTURE_PASS' if ok else 'SMALL_WORLDS_CAPTURE_FAIL')
    ue.EditorPythonScripting.set_keep_python_script_alive(False)
    ue.SystemLibrary.quit_editor()


def tick(delta):
    if state['busy']:
        return
    state['busy'] = True
    try:
        if state['index'] == len(jobs):
            finish(True)
            return
        map_name, camera_name, filename = jobs[state['index']]
        now = time.monotonic()
        if state['phase'] == 'load':
            sw.LEVELS.load_level(sw.ROOT + '/Maps/' + map_name)
            cam = next(a for a in sw.ACTORS.get_all_level_actors() if a.get_actor_label() == camera_name)
            sw.LEVELS.pilot_level_actor(cam)
            ue.SystemLibrary.execute_console_command(None, 'r.ScreenPercentage 100')
            state.update(phase='warm', at=now)
        elif state['phase'] == 'warm' and now - state['at'] > 15:
            state.update(phase='capture', at=now)
            ue.AutomationLibrary.take_high_res_screenshot(1600, 900, str(out / filename))
        elif state['phase'] == 'capture' and now - state['at'] > 5:
            if not (out / filename).exists():
                if now - state['at'] > 30:
                    raise RuntimeError('Screenshot did not arrive: ' + filename)
                return
            state.update(index=state['index']+1, phase='load', at=now)
    except Exception:
        ue.log_error(traceback.format_exc())
        finish(False)
    finally:
        state['busy'] = False


state['handle'] = ue.register_slate_post_tick_callback(tick)
