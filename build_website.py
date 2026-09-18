from pathlib import Path
import sys
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'source'))
from build_tracks import build
from build_cvs import make_cv
make_cv('marketing',root,track_root=root)
build('marketing',root)
