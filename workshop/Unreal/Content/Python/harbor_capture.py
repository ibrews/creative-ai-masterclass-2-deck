"""Capture the real Harbor City and gallery on Slate ticks, then close this editor."""
from pathlib import Path
import json,os,time,traceback
import unreal as ue
import small_worlds as sw
out=Path(os.environ['SMALL_WORLDS_EVIDENCE'])
jobs=[('05_HarborCity','HK_Cam_City','07-harbor-city.png'),('05_HarborCity','HK_Cam_Market','08-harbor-market.png'),('05_HarborCity','HK_Cam_Forage','09-forage-monument.png'),('06_KitGallery','HK_Cam_Gallery','10-kit-gallery.png')]
state = {'index': 0, 'phase': 'load', 'at': time.monotonic(), 'busy': False, 'handle': None}
ue.EditorPythonScripting.set_keep_python_script_alive(True)


def finish(ok):
    ue.unregister_slate_post_tick_callback(state['handle'])
    (out / 'harbor-capture-result.json').write_text(json.dumps({'passed': ok, 'files': [j[2] for j in jobs], 'engine': ue.SystemLibrary.get_engine_version()}, indent=2))
    ue.log('HARBOR_CAPTURE_PASS' if ok else 'HARBOR_CAPTURE_FAIL')
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
