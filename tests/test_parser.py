from pathlib import Path

import pytest

from gendiff.parser import parse_file

TEST_DATA = Path(__file__).parent / "test_data"

def test_parse_yaml():
    result = parse_file(TEST_DATA / "file2.yml")
    assert result == {"timeout": 20, "verbose": True, "host": "hexlet.io"}


def test_parse_unsupported_extension():
    with pytest.raises(ValueError):
        parse_file(TEST_DATA / "expected_flat.txt")