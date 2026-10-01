import json
from pathlib import Path

import yaml

PARSERS = {
    ".json": json.loads,
    ".yml": yaml.safe_load,
    ".yaml": yaml.safe_load,
}


def parse_file(path):
    extension = Path(path).suffix.lower()
    if extension not in PARSERS:
        raise ValueError(f"Unsupported file format: {extension}")
    with open(path, encoding="utf-8") as file:
        return PARSERS[extension](file.read())