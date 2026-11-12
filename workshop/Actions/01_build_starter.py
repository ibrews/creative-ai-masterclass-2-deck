from pathlib import Path
import sys
import unreal
p = str(Path(unreal.Paths.project_dir()) / "Content" / "Python")
if p not in sys.path: sys.path.insert(0, p)
import small_worlds
import importlib
importlib.reload(small_worlds)
small_worlds.build("starter")
