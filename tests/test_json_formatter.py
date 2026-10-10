import json

from gendiff.formatters.json_formatter import format_json


def test_format_json_is_valid_and_keeps_tree():
    diff = [
        {"key": "a", "type": "added", "value": None},
        {"key": "b", "type": "changed", "old_value": 1, "new_value": "é"},
    ]
    result = format_json(diff)
    assert json.loads(result) == diff
    assert "é" in result