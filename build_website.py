"""Rebuild the checked-in static website using the editable content sources."""
from pathlib import Path
import os
import subprocess
import sys

root = Path(__file__).resolve().parent
env = dict(os.environ, MARKETING_OUTPUT_DIR=str(root))
for script in ("build_site.py", "refine_site.py", "business_context.py", "section_experiences.py"):
    subprocess.run([sys.executable, str(root / "source" / script)], env=env, check=True)
print("Website rebuilt in website/.")
