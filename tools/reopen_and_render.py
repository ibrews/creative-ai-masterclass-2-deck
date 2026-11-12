"""Independent saved reopen, followed by native MRQ rendering in this second process."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_reopen
import render_native_movie
