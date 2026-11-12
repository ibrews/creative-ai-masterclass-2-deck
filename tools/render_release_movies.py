"""Independent saved reopen and two actual MRQ movies for the classroom release."""
from pathlib import Path
import os,sys,json
import unreal as ue
sys.path.insert(0,str(Path(__file__).resolve().parent))
import verify_reopen
import harbor_kit as hk
out=Path(os.environ['SMALL_WORLDS_EVIDENCE'])
levels=ue.get_editor_subsystem(ue.LevelEditorSubsystem)
actors=ue.get_editor_subsystem(ue.EditorActorSubsystem)
levels.load_level('/Game/SmallWorlds/Maps/05_HarborCity')
city=hk.verify_city()
bridges=[a for a in actors.get_all_level_actors() if a.get_actor_label().startswith('HK_bridge_') and '__' not in a.get_actor_label()]
assert len(bridges)==6
for a in bridges:
 r=a.get_actor_rotation()
 assert abs(r.pitch)<.1 and abs(r.yaw-90)<.1 and abs(r.roll)<.1, 'Bridge tilt: '+str(r)
seq=ue.load_asset('/Game/SmallWorlds/Cinematics/LS_HarborCity')
assert seq.get_display_rate().numerator==24 and seq.get_playback_end()==288
cuts=[t for t in seq.get_tracks() if isinstance(t,ue.MovieSceneCameraCutTrack)]
assert len(cuts)==1 and len(cuts[0].get_sections())==3
levels.load_level('/Game/SmallWorlds/Maps/06_KitGallery')
parts=json.loads(hk.CATALOG.read_text())['parts']
labels={a.get_actor_label() for a in actors.get_all_level_actors()}
assert all('KIT_%02d_%s'%(i+1,p) in labels for i,p in enumerate(parts))
(out/'final-independent-reopen.json').write_text(json.dumps({'engine':ue.SystemLibrary.get_engine_version(),'city':city,'bridge_rotations':'Six horizontal decks, yaw 90, PASS','gallery_parts':list(parts),'sequence':{'fps':24,'frames':288,'camera_cuts':3}},indent=2))
sub=ue.get_editor_subsystem(ue.MoviePipelineQueueSubsystem)
queue=sub.get_queue();queue.delete_all_jobs()
for name,map_name,seq_name in [('paper-city','04_Cinematic','LS_LanternFestival'),('harbor-city','05_HarborCity','LS_HarborCity')]:
 job=queue.allocate_new_job(ue.MoviePipelineExecutorJob);job.job_name=name
 job.map=ue.SoftObjectPath('/Game/SmallWorlds/Maps/'+map_name+'.'+map_name)
 job.sequence=ue.SoftObjectPath('/Game/SmallWorlds/Cinematics/'+seq_name+'.'+seq_name)
 config=job.get_configuration();output=config.find_or_add_setting_by_class(ue.MoviePipelineOutputSetting)
 output.output_directory=ue.DirectoryPath(str(out/'release-movies'/name))
 output.file_name_format=name+'.{frame_number}'
 output.output_resolution=ue.IntPoint(1280,720);output.use_custom_frame_rate=True;output.output_frame_rate=ue.FrameRate(24,1)
 config.find_or_add_setting_by_class(ue.MoviePipelineDeferredPassBase)
 config.find_or_add_setting_by_class(ue.MoviePipelineImageSequenceOutput_PNG)
 aa=config.find_or_add_setting_by_class(ue.MoviePipelineAntiAliasingSetting)
 aa.engine_warm_up_count=32;aa.render_warm_up_count=8;aa.spatial_sample_count=1;aa.temporal_sample_count=1
ue.EditorPythonScripting.set_keep_python_script_alive(True)
def done(executor,success):
 (out/os.environ.get('CLASS_RENDER_RESULT','release-movies-result.txt')).write_text('PASS' if success else 'FAIL')
 ue.log('RELEASE_MOVIES_PASS' if success else 'RELEASE_MOVIES_FAIL')
 ue.EditorPythonScripting.set_keep_python_script_alive(False);ue.SystemLibrary.quit_editor()
executor=ue.MoviePipelinePIEExecutor();executor.on_executor_finished_delegate.add_callable_unique(done)
sub.render_queue_with_executor_instance(executor)
