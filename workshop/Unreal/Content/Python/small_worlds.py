"""Small Worlds, Part 2. Run inside Unreal Editor, never system Python.

Original classroom geometry is assembled from Unreal's built-in basic shapes.
Each action creates a different map; an existing map is never overwritten.
"""
from pathlib import Path
import json
import math
import unreal as ue

PROJECT = Path(ue.Paths.project_dir()).resolve()
WORKSHOP = PROJECT.parent
CONFIG = WORKSHOP / "Studio" / "design.json"
ROOT = "/Game/SmallWorlds"
ACTORS = ue.get_editor_subsystem(ue.EditorActorSubsystem)
ASSETS = ue.get_editor_subsystem(ue.EditorAssetSubsystem)
LEVELS = ue.get_editor_subsystem(ue.LevelEditorSubsystem)
MESHES = {n: ue.load_asset('/Engine/BasicShapes/' + n) for n in ['Cube', 'Cylinder', 'Cone', 'Sphere']}


def material(name, color, metallic=0.0, roughness=0.65, glow=0.0):
    path = ROOT + '/Materials/M_' + name
    if ASSETS.does_asset_exist(path):
        return ue.load_asset(path)
    mat = ue.AssetToolsHelpers.get_asset_tools().create_asset('M_' + name, ROOT + '/Materials', ue.Material, ue.MaterialFactoryNew())
    lib = ue.MaterialEditingLibrary
    rgb = lib.create_material_expression(mat, ue.MaterialExpressionConstant3Vector, -400, 0)
    rgb.set_editor_property('constant', ue.LinearColor(*color, 1.0))
    lib.connect_material_property(rgb, '', ue.MaterialProperty.MP_BASE_COLOR)
    for prop, value in [(ue.MaterialProperty.MP_ROUGHNESS, roughness), (ue.MaterialProperty.MP_METALLIC, metallic)]:
        node = lib.create_material_expression(mat, ue.MaterialExpressionConstant, -200, 100)
        node.set_editor_property('r', value)
        lib.connect_material_property(node, '', prop)
    if glow:
        bright = lib.create_material_expression(mat, ue.MaterialExpressionConstant3Vector, -400, 200)
        bright.set_editor_property('constant', ue.LinearColor(*(c * glow for c in color), 1.0))
        lib.connect_material_property(bright, '', ue.MaterialProperty.MP_EMISSIVE_COLOR)
    lib.recompile_material(mat)
    ASSETS.save_loaded_asset(mat)
    return mat


def mesh(label, xyz, size, mat, shape='Cube', rotation=(0, 0, 0)):
    actor = ACTORS.spawn_actor_from_class(ue.StaticMeshActor, ue.Vector(*xyz), ue.Rotator(*rotation))
    actor.set_actor_label(label)
    actor.set_folder_path('SmallWorlds/Geometry')
    comp = actor.static_mesh_component
    comp.set_mobility(ue.ComponentMobility.MOVABLE)
    comp.set_static_mesh(MESHES[shape])
    comp.set_material(0, mat)
    # Engine basic shapes have 100 cm bounds on each axis, except the cone/cylinder Z is also 100.
    actor.set_actor_scale3d(ue.Vector(*(v / 100.0 for v in size)))
    return actor


def light(label, xyz, intensity, color, radius=650):
    actor = ACTORS.spawn_actor_from_class(ue.PointLight, ue.Vector(*xyz))
    actor.set_actor_label(label)
    actor.set_folder_path('SmallWorlds/Lights')
    comp = actor.get_component_by_class(ue.PointLightComponent)
    comp.set_mobility(ue.ComponentMobility.MOVABLE)
    comp.set_editor_property('intensity', float(intensity))
    comp.set_editor_property('attenuation_radius', float(radius))
    comp.set_editor_property('light_color', ue.Color(r=color[0], g=color[1], b=color[2], a=255))
    return actor


def camera(label, xyz, target, focal=35.0):
    loc = ue.Vector(*xyz)
    actor = ACTORS.spawn_actor_from_class(ue.CineCameraActor, loc, ue.MathLibrary.find_look_at_rotation(loc, ue.Vector(*target)))
    actor.set_actor_label(label)
    actor.set_folder_path('SmallWorlds/Cameras')
    comp = actor.get_cine_camera_component()
    comp.set_editor_property('current_focal_length', focal)
    comp.set_editor_property('current_aperture', 8.0)
    comp.set_editor_property('post_process_blend_weight', 0.0)
    focus = comp.get_editor_property('focus_settings')
    focus.set_editor_property('focus_method', ue.CameraFocusMethod.DISABLE)
    comp.set_editor_property('focus_settings', focus)
    return actor


def seq_transform(binding, keys, end=12.0):
    track = binding.add_track(ue.MovieScene3DTransformTrack)
    section = track.add_section()
    section.set_range_seconds(0.0, end)
    channels = section.get_all_channels()
    for seconds, xyz, rot, scale in keys:
        values = list(xyz) + [rot[2], rot[0], rot[1]] + list(scale)
        for ch, value in zip(channels, values):
            ch.add_key(ue.FrameNumber(round(seconds * 24)), float(value), interpolation=ue.MovieSceneKeyInterpolation.LINEAR)


def sequence(cams, sculpture):
    path = ROOT + '/Cinematics/LS_LanternFestival'
    if ASSETS.does_asset_exist(path):
        raise RuntimeError('Sequence already exists. Preserve it and use a fresh project copy before rebuilding.')
    seq = ue.AssetToolsHelpers.get_asset_tools().create_asset('LS_LanternFestival', ROOT + '/Cinematics', ue.LevelSequence, ue.LevelSequenceFactoryNew())
    seq.set_display_rate(ue.FrameRate(24, 1))
    seq.set_playback_start(0)
    seq.set_playback_end(288)
    cuts = seq.add_track(ue.MovieSceneCameraCutTrack)
    for i, cam in enumerate(cams):
        binding = seq.add_possessable(cam)
        cut = cuts.add_section()
        cut.set_range_seconds(float(i * 4), float((i + 1) * 4))
        cut.set_camera_binding_id(ue.MovieSceneSequenceExtensions.get_binding_id(seq, binding))
        start = cam.get_actor_location()
        rot = cam.get_actor_rotation()
        xyz = (start.x, start.y, start.z)
        r = (rot.pitch, rot.yaw, rot.roll)
        finish = (start.x + 95, start.y + 65, start.z + 25)
        seq_transform(binding, [(i * 4, xyz, r, (1, 1, 1)), ((i + 1) * 4, finish, r, (1, 1, 1))])
    binding = seq.add_possessable(sculpture)
    p = sculpture.get_actor_location()
    s = sculpture.get_actor_scale3d()
    seq_transform(binding, [(0, (p.x, p.y, p.z), (0, 0, 0), (s.x, s.y, s.z)),
                             (6, (p.x, p.y, p.z + 45), (0, 180, 0), (s.x, s.y, s.z)),
                             (12, (p.x, p.y, p.z), (0, 360, 0), (s.x, s.y, s.z))])
    ue.EditorLoadingAndSavingUtils.save_packages([seq.get_outermost()], only_dirty=False)
    return seq


def build(stage='starter'):
    cfg = json.loads(CONFIG.read_text(encoding='utf-8'))
    if stage not in ['starter', 'dusk', 'festival', 'cinematic']:
        raise ValueError(stage)
    names = dict(starter='01_PaperCity', dusk='02_Dusk', festival='03_LanternFestival', cinematic='04_Cinematic')
    path = ROOT + '/Maps/' + names[stage]
    if ASSETS.does_asset_exist(path):
        raise RuntimeError(path + ' already exists. Open it instead, or duplicate the workshop folder before experimenting.')
    if not LEVELS.new_level(path):
        raise RuntimeError('Could not create ' + path)
    dusk = stage != 'starter'
    festival = stage in ['festival', 'cinematic']
    ivory = material('Ivory', (.88, .72, .46))
    clay = material('Terracotta', (.62, .17, .085))
    jade = material('Jade', (.035, .33, .24))
    dark = material('Canal', (.012, .075, .13), metallic=.55, roughness=.22)
    ground = material('Quay', (.14, .20, .21))
    brass = material('Brass', (.76, .36, .07), metallic=.75, roughness=.3)
    leaf = material('Sage', (.13, .30, .19))
    gold = material('LanternGlowDusk' if dusk else 'LanternGlowDay', (1, .36, .055), glow=cfg['lantern_glow'] if dusk else .2)
    cyan = material('Sculpture', (.025, .58, .72), metallic=.5, roughness=.25, glow=.15)
    mesh('SW_Canal', (0, 0, -45), (2000, 1300, 65), dark)
    mesh('SW_NorthQuay', (0, 240, -5), (1800, 580, 40), ground)
    mesh('SW_SouthQuay', (0, -480, -5), (1800, 280, 40), ground)
    mesh('SW_Platform', (0, 0, -100), (2100, 1400, 45), clay)
    for i, (x, h) in enumerate(zip([-490, 0, 490], cfg['tower_heights_cm']), 1):
        mesh('SW_Tower_%d' % i, (x, 220, h / 2), (250, 220, h), [ivory, clay, ivory][i-1])
        for level in range(1, int(h // 80)):
            for dx in [-65, 65]:
                mesh('SW_Window_%d_%d_%d' % (i, level, dx), (x + dx, 108, level * 75), (38, 8, 36), gold)
        # Pair of sloped planes forms a folded paper roof. Deliberately readable construction.
        for side in [-1, 1]:
            mesh('SW_Roof_%d_%d' % (i, side), (x + side * 70, 220, h + 32), (165, 250, 12), brass, rotation=(-side * 30, 0, 0))
    for bx in [-490, 490]:
        mesh('SW_Bridge_%d' % bx, (bx, -170, 12), (180, 530, 25), ivory)
        for dx in [-88, 88]:
            mesh('SW_Rail_%d_%d' % (bx, dx), (bx + dx, -170, 106), (9, 530, 12), jade)
            for by in [-390, -170, 55]:
                mesh('SW_Post_%d_%d_%d' % (bx, dx, by), (bx + dx, by, 55), (10, 10, 100), jade)
    # Reusable prop recipe: a lantern is a post, cap and emissive globe.
    for i, x in enumerate([-750, -250, 250, 750]):
        mesh('SW_LanternPost_%d' % i, (x, -470, 130), (10, 10, 260), brass, 'Cylinder')
        mesh('SW_LanternCap_%d' % i, (x, -470, 270), (60, 60, 15), brass)
        mesh('SW_Lantern_%d' % i, (x, -470, 238), (38, 38, 50), gold, 'Sphere')
        if dusk:
            light('SW_LanternLight_%d' % i, (x, -455, 235), cfg['lantern_intensity'], (255, 157, 67), 500)
    sculpture = mesh('SW_FloatingSculpture', (0, -210, 160), (115, 115, 115), cyan, 'Cube', (0, 45, 0))
    mesh('SW_SculpturePlinth', (0, -210, 25), (170, 170, 35), ivory, 'Cylinder')
    if festival:
        for i, x in enumerate([-760, -250, 250, 760]):
            mesh('SW_TreeTrunk_%d' % i, (x, 500, 80), (25, 25, 140), brass, 'Cylinder')
            for j, (z, radius) in enumerate([(150, 130), (215, 105), (270, 75)]):
                mesh('SW_TreeCrown_%d_%d' % (i, j), (x, 500, z), (radius, radius, 125), leaf, 'Cone')
        for i, x in enumerate([-600, 600]):
            mesh('SW_BenchSeat_%d' % i, (x, -530, 55), (165, 50, 12), ivory)
            mesh('SW_BenchBack_%d' % i, (x, -550, 90), (165, 10, 60), jade)
            for dx in [-60, 60]:
                mesh('SW_BenchLeg_%d_%d' % (i, dx), (x + dx, -530, 30), (12, 40, 50), brass)
        for i, x in enumerate(range(-700, 701, 140)):
            z = 395 - 70 * (1 - (abs(x) / 700)**2)
            mesh('SW_HangingLantern_%d' % i, (x, -100, z), (32, 32, 44), gold, 'Sphere')
            if i % 3 == 0:
                light('SW_FestivalLight_%d' % i, (x, -100, z), 45, (255, 137, 45), 420)
        # Nine individual stepping stones and boats give foreground scale cues.
        for i, x in enumerate(range(-600, 601, 150)):
            mesh('SW_SteppingStone_%d' % i, (x, -300, 2), (70, 60, 14), ivory, 'Cylinder')
        for i, x in enumerate([-235, 220]):
            mesh('SW_Boat_%d' % i, (x, -80, 8), (130, 58, 28), clay, 'Sphere')
            mesh('SW_BoatMast_%d' % i, (x, -80, 80), (6, 6, 135), brass, 'Cylinder')
            mesh('SW_BoatSail_%d' % i, (x+25, -80, 100), (55, 6, 85), ivory)
    atmosphere = ACTORS.spawn_actor_from_class(ue.SkyAtmosphere, ue.Vector(0, 0, 0))
    atmosphere.set_actor_label('SW_Atmosphere')
    sky = ACTORS.spawn_actor_from_class(ue.SkyLight, ue.Vector(0, 0, 600))
    sky.set_actor_label('SW_SkyLight')
    sky.light_component.set_mobility(ue.ComponentMobility.MOVABLE)
    sky.light_component.set_editor_property('intensity', .8 if dusk else 1.8)
    sun = ACTORS.spawn_actor_from_class(ue.DirectionalLight, ue.Vector(0, 0, 900), ue.Rotator(-32, -35, 0))
    sun.set_actor_label('SW_KeyLight')
    sun.get_component_by_class(ue.DirectionalLightComponent).set_mobility(ue.ComponentMobility.MOVABLE)
    sun.get_component_by_class(ue.DirectionalLightComponent).set_editor_property('atmosphere_sun_light', True)
    sun.get_component_by_class(ue.DirectionalLightComponent).set_editor_property('intensity', 2.0 if dusk else 5.0)
    sun.get_component_by_class(ue.DirectionalLightComponent).set_editor_property('light_color', ue.Color(r=255, g=181, b=119, a=255) if dusk else ue.Color(r=235, g=243, b=255, a=255))
    pp = ACTORS.spawn_actor_from_class(ue.PostProcessVolume, ue.Vector(0, 0, 0))
    pp.set_actor_label('SW_Exposure')
    pp.set_editor_property('unbound', True)
    settings = pp.get_editor_property('settings')
    for key, value in [('override_auto_exposure_method', True), ('auto_exposure_method', ue.AutoExposureMethod.AEM_MANUAL),
                       ('override_auto_exposure_bias', True), ('auto_exposure_bias', cfg['exposure_bias']),
                       ('override_auto_exposure_apply_physical_camera_exposure', True), ('auto_exposure_apply_physical_camera_exposure', False)]:
        settings.set_editor_property(key, value)
    pp.set_editor_property('settings', settings)
    cams = [camera('SW_Cam_Wide', (1850, -2450, 1500), (0, 0, 170), 38),
            camera('SW_Cam_Bridge', (-1000, -1350, 370), (-400, 20, 140), 40),
            camera('SW_Cam_Sculpture', (530, -750, 310), (0, -210, 175), 45)]
    if stage == 'cinematic':
        sequence(cams, sculpture)
    LEVELS.save_current_level()
    ue.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
    LEVELS.set_current_level_by_name(names[stage]) if hasattr(LEVELS, 'set_current_level_by_name') else None
    ue.EditorLevelLibrary.set_level_viewport_camera_info(ue.Vector(1850, -2450, 1500), cams[0].get_actor_rotation())
    result = verify(stage)
    ue.log('SMALL_WORLDS_PASS ' + json.dumps(result))
    return result


def verify(stage=None):
    actors = [a for a in ACTORS.get_all_level_actors() if a.get_actor_label().startswith('SW_')]
    by_label = {a.get_actor_label(): a for a in actors}
    cfg = json.loads(CONFIG.read_text(encoding='utf-8'))
    assert len(actors) >= 50, 'Expected at least 50 authored actors'
    for i, height in enumerate(cfg['tower_heights_cm'], 1):
        actor = by_label['SW_Tower_%d' % i]
        assert abs(actor.get_actor_scale3d().z * 100 - height) < .1, 'Tower height mismatch'
    assert all('SW_Cam_' + n in by_label for n in ['Wide', 'Bridge', 'Sculpture'])
    saved = ue.EditorLevelLibrary.get_editor_world().get_path_name().split('.')[0]
    if stage is None:
        stage = next((key for key, name in dict(starter='01_PaperCity', dusk='02_Dusk', festival='03_LanternFestival', cinematic='04_Cinematic').items() if saved.endswith('/' + name)), 'custom')
    result = {'stage': stage, 'actors': len(actors), 'tower_heights_cm': cfg['tower_heights_cm'], 'map': saved,
              'engine': ue.SystemLibrary.get_engine_version(), 'visual_acceptance': 'Inspect the actual editor view yourself.'}
    receipts = WORKSHOP / 'Studio' / 'receipts'
    receipts.mkdir(parents=True, exist_ok=True)
    (receipts / ((stage or 'current') + '.json')).write_text(json.dumps(result, indent=2), encoding='utf-8')
    return result
