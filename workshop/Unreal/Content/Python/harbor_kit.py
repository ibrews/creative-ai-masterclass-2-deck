"""Original modular Harbor City kit. Run in the Unreal Editor, not system Python.

A part is a JSON recipe of named mesh components in centimeters. spawn_part()
instantiates only the selected part; build_city() composes those recipes.
All assets from another creator must be supplied by the learner, never guessed.
"""
from pathlib import Path
import json
import math
import unreal as ue
import small_worlds as sw

WORKSHOP = Path(ue.Paths.project_dir()).resolve().parent
CATALOG = WORKSHOP / 'Studio' / 'harbor-kit.json'
LAYOUT = WORKSHOP / 'Studio' / 'harbor-city.json'
TOKEN = '/Game/ForageBetaSample/SM_ForageToken.SM_ForageToken'


def palette():
    return {
        'ivory': sw.material('Ivory', (.88, .72, .46)),
        'clay': sw.material('Terracotta', (.62, .17, .085)),
        'jade': sw.material('Jade', (.035, .33, .24)),
        'canal': sw.material('Canal', (.012, .075, .13), metallic=.55, roughness=.22),
        'quay': sw.material('Quay', (.14, .20, .21)),
        'brass': sw.material('Brass', (.76, .36, .07), metallic=.75, roughness=.3),
        'sage': sw.material('Sage', (.13, .30, .19)),
        'glow': sw.material('HarborWarm', (1, .32, .055), glow=2.4),
        'cyan': sw.material('HarborTeal', (.015, .35, .50), glow=.65),
        'rose': sw.material('HarborRose', (.45, .055, .14), glow=.15),
    }


def spawn_part(part_id, x=0, y=0, z=0, yaw=0, name=None):
    """Use exact catalog IDs. Returns all native actors for selection/revision."""
    catalog = json.loads(CATALOG.read_text())
    part = catalog['parts'][part_id]
    mats = palette()
    label = name or 'HK_' + part_id
    angle = math.radians(yaw)
    actors = []
    for i, c in enumerate(part['components']):
        px, py, pz = c['at']
        loc = (x + px*math.cos(angle)-py*math.sin(angle),
               y + px*math.sin(angle)+py*math.cos(angle), z+pz)
        rotation = c.get('rotation', [0, 0, 0])
        rot = (rotation[0], rotation[1]+yaw, rotation[2])
        a = sw.mesh(label if i == 0 else label+'__'+c['name'], loc, c['size'],
                    mats[c['material']], c.get('shape', 'Cube'), rot)
        a.set_folder_path('HarborKit/'+label)
        if actors:
            a.attach_to_actor(actors[0], '', ue.AttachmentRule.KEEP_WORLD,
                              ue.AttachmentRule.KEEP_WORLD, ue.AttachmentRule.KEEP_WORLD, False)
        actors.append(a)
    return actors


def setup_light():
    sky = sw.ACTORS.spawn_actor_from_class(ue.SkyLight, ue.Vector(0, 0, 1000))
    sky.set_actor_label('HK_SkyFill')
    sky.light_component.set_mobility(ue.ComponentMobility.MOVABLE)
    sky.light_component.set_editor_property('intensity', 1.2)
    sun = sw.ACTORS.spawn_actor_from_class(ue.DirectionalLight, ue.Vector(0, 0, 1300), ue.Rotator(pitch=-32, yaw=-35, roll=0))
    sun.set_actor_label('HK_WarmKey')
    c = sun.get_component_by_class(ue.DirectionalLightComponent)
    c.set_mobility(ue.ComponentMobility.MOVABLE)
    c.set_editor_property('intensity', 3.5)
    c.set_editor_property('light_color', ue.Color(r=255, g=197, b=154, a=255))
    fill = sw.ACTORS.spawn_actor_from_class(ue.DirectionalLight, ue.Vector(0, 0, 1400), ue.Rotator(pitch=-25, yaw=145, roll=0))
    fill.set_actor_label('HK_CoolFill')
    fc = fill.get_component_by_class(ue.DirectionalLightComponent)
    fc.set_mobility(ue.ComponentMobility.MOVABLE)
    fc.set_editor_property('intensity', 2.0)
    fc.set_editor_property('light_color', ue.Color(r=155, g=205, b=255, a=255))
    pp = sw.ACTORS.spawn_actor_from_class(ue.PostProcessVolume, ue.Vector())
    pp.set_actor_label('HK_Exposure')
    pp.set_editor_property('unbound', True)
    s = pp.get_editor_property('settings')
    for k, v in [('override_auto_exposure_method', True), ('auto_exposure_method', ue.AutoExposureMethod.AEM_MANUAL),
                 ('override_auto_exposure_bias', True), ('auto_exposure_bias', .2),
                 ('override_auto_exposure_apply_physical_camera_exposure', True), ('auto_exposure_apply_physical_camera_exposure', False), ('override_lens_flare_intensity', True), ('lens_flare_intensity', 0.0), ('override_bloom_intensity', True), ('bloom_intensity', .25)]:
        s.set_editor_property(k, v)
    pp.set_editor_property('settings', s)


def token_monument():
    token = ue.load_asset(TOKEN)
    if not token:
        raise RuntimeError('Run Forage Guided Tutorial and approve its sample import first. Expected '+TOKEN)
    a = sw.ACTORS.spawn_actor_from_class(ue.StaticMeshActor, ue.Vector(0, 0, 650))
    a.set_actor_label('HK_ForageToken_Hero')
    a.set_folder_path('HarborKit/Forage imported practice asset')
    a.static_mesh_component.set_static_mesh(token)
    a.set_actor_scale3d(ue.Vector(5, 5, 5))
    return a


def _new_map(name):
    path = sw.ROOT+'/Maps/'+name
    if sw.ASSETS.does_asset_exist(path):
        raise RuntimeError(path+' exists. Preserve it and use a fresh Starter or a new map name.')
    if not sw.LEVELS.new_level(path):
        raise RuntimeError('Could not create '+path)
    return path


def build_city():
    # Prove the Forage import before creating a partial map.
    if not ue.load_asset(TOKEN):
        raise RuntimeError('Import the Forage practice sample before building Harbor City. See workbook Forage chapter.')
    layout = json.loads(LAYOUT.read_text())
    path = _new_map('05_HarborCity')
    mats = palette()
    sw.mesh('HK_Canal', (0, 0, -70), (5700, 4300, 95), mats['canal'])
    sw.mesh('HK_DioramaBase', (0, 0, -155), (5900, 4500, 100), mats['brass'])
    for p in layout['placements']:
        spawn_part(p['part'], *p['at'], yaw=p.get('yaw', 0), name=p['name'])
    hero = token_monument()
    setup_light()
    for i, (x, y) in enumerate([(-1550, -1250), (1550, -1250), (-1550, 900), (1550, 900)]):
        sw.light('HK_DistrictLight_'+str(i), (x, y, 320), 120, (255, 155, 70), 1300)
    wide = sw.camera('HK_Cam_City', (5700, -7400, 5400), (0, 0, 360), 38)
    market = sw.camera('HK_Cam_Market', (-2000, -2650, 650), (-450, -500, 230), 32)
    detail = sw.camera('HK_Cam_Forage', (2000, -3500, 1600), (0, 0, 610), 32)
    sw.sequence([wide, market, detail], hero, "LS_HarborCity")
    sw.LEVELS.save_current_level()
    ue.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
    result = verify_city()
    ue.log('HARBOR_CITY_PASS '+json.dumps(result))
    return result


def build_gallery():
    path = _new_map('06_KitGallery')
    mats = palette()
    sw.mesh('HK_GalleryFloor', (0, 0, -50), (6500, 4300, 80), mats['quay'])
    parts = json.loads(CATALOG.read_text())['parts']
    for i, part in enumerate(parts):
        x, y = (i%4-1.5)*1450, (i//4-1)*1300
        sw.mesh('HK_Plinth_'+part, (x, y, 0), (1200, 1050, 35), mats['ivory'])
        spawn_part(part, x, y, 20, name='KIT_%02d_%s'%(i+1, part))
    setup_light()
    sw.camera('HK_Cam_Gallery', (6100, -7700, 6500), (0, 0, 230), 38)
    sw.LEVELS.save_current_level()
    ue.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
    result = {'map':path, 'part_types':len(parts), 'parts':list(parts)}
    ue.log('HARBOR_GALLERY_PASS '+json.dumps(result))
    return result


def verify_city():
    all_actors = sw.ACTORS.get_all_level_actors()
    names = {a.get_actor_label():a for a in all_actors}
    layout = json.loads(LAYOUT.read_text())
    missing = [p['name'] for p in layout['placements'] if p['name'] not in names]
    assert not missing, 'Missing anchors: '+str(missing)
    assert 'HK_ForageToken_Hero' in names, 'Forage sample not used'
    hero = names['HK_ForageToken_Hero'].static_mesh_component.static_mesh
    assert hero.get_path_name() == TOKEN
    for camera in ['City', 'Market', 'Forage']:
        assert 'HK_Cam_'+camera in names
    return {'map':sw.ROOT+'/Maps/05_HarborCity', 'placements':len(layout['placements']),
            'actors':len([a for a in all_actors if a.get_actor_label().startswith('HK_')]),
            'forage_mesh':hero.get_path_name(), 'part_types':len(json.loads(CATALOG.read_text())['parts'])}
