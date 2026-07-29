"""File reading utilities for test automation."""

import json
import yaml
from pathlib import Path
from typing import Any, Dict, Union


def read_json(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Read JSON file and return as dictionary."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def read_yaml(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Read YAML file and return as dictionary."""
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def read_csv(file_path: Union[str, Path]) -> list:
    """Read CSV file and return as list of dictionaries."""
    import csv

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def read_text(file_path: Union[str, Path]) -> str:
    """Read text file and return content."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
