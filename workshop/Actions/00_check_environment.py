import unreal
from pathlib import Path
print("SMALL_WORLDS_ENVIRONMENT", unreal.SystemLibrary.get_engine_version(), Path(unreal.Paths.project_dir()).resolve().parent)
