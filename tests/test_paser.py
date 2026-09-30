from pathlib import Path

from gendiff.parser import parse_file

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_json():
    result = parse_file(FIXTURES / "file2.json")
    assert result == {"timeout": 20, "verbose": True, "host": "hexlet.io"}