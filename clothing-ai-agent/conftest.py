import sys
from pathlib import Path

# Ensure pytest finds project modules (models, data, agent, tools) on import.
ROOT = Path(__file__).parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
