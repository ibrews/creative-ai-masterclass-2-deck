import unreal, sys
from pathlib import Path
p=str(Path(unreal.Paths.project_dir())/"Content"/"Python")
if p not in sys.path: sys.path.insert(0,p)
import small_worlds
print("SMALL_WORLDS_VERIFY",small_worlds.verify())
