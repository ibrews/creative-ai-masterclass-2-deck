"""Render the saved native LevelSequence through Movie Render Queue."""
from pathlib import Path
import os
import unreal as ue

out = Path(os.environ['SMALL_WORLDS_EVIDENCE']) / 'movie-frames'
out.mkdir(parents=True, exist_ok=True)
ue.get_editor_subsystem(ue.LevelEditorSubsystem).load_level('/Game/SmallWorlds/Maps/04_Cinematic')
sub = ue.get_editor_subsystem(ue.MoviePipelineQueueSubsystem)
queue = sub.get_queue()
queue.delete_all_jobs()
job = queue.allocate_new_job(ue.MoviePipelineExecutorJob)
job.job_name = 'SmallWorlds12Seconds'
job.map = ue.SoftObjectPath('/Game/SmallWorlds/Maps/04_Cinematic')
job.sequence = ue.SoftObjectPath('/Game/SmallWorlds/Cinematics/LS_LanternFestival')
config = job.get_configuration()
output = config.find_or_add_setting_by_class(ue.MoviePipelineOutputSetting)
output.output_directory = ue.DirectoryPath(str(out))
output.file_name_format = 'paper-city.{frame_number}'
output.output_resolution = ue.IntPoint(1280, 720)
output.use_custom_frame_rate = True
output.output_frame_rate = ue.FrameRate(24, 1)
config.find_or_add_setting_by_class(ue.MoviePipelineDeferredPassBase)
config.find_or_add_setting_by_class(ue.MoviePipelineImageSequenceOutput_PNG)
aa = config.find_or_add_setting_by_class(ue.MoviePipelineAntiAliasingSetting)
aa.engine_warm_up_count = 32
aa.render_warm_up_count = 8
aa.spatial_sample_count = 1
aa.temporal_sample_count = 1
ue.EditorPythonScripting.set_keep_python_script_alive(True)


def done(executor, success):
    (out.parent / 'movie-result.txt').write_text('PASS' if success else 'FAIL')
    ue.log('SMALL_WORLDS_MOVIE_PASS' if success else 'SMALL_WORLDS_MOVIE_FAIL')
    ue.EditorPythonScripting.set_keep_python_script_alive(False)
    ue.SystemLibrary.quit_editor()


executor = ue.MoviePipelinePIEExecutor()
executor.on_executor_finished_delegate.add_callable_unique(done)
sub.render_queue_with_executor_instance(executor)
