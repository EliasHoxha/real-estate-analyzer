from pathlib import Path
import yaml

def load_yaml(path: str | Path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def ensure_dirs(*dirs):
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)