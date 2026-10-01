from pathlib import Path

from gendiff.parser import parse_file

TEST_DATA = Path(__file__).parent / "test_data"


def test_parse_json():
    result = parse_file(TEST_DATA / "file2.json")
    assert result == {"timeout": 20, "verbose": True, "host": "hexlet.io"}