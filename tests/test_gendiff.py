import json
from pathlib import Path

import pytest

from gendiff import generate_diff

TEST_DATA = Path(__file__).parent / "test_data"


def read_expected(name):
    return (TEST_DATA / name).read_text(encoding="utf-8").strip()


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        ("file1.json", "file2.json", "expected_flat.txt"),
        ("file2.json", "file1.json", "expected_flat_reversed.txt"),
        ("file1.yml", "file2.yml", "expected_flat.txt"),
        ("file1.yml", "file2.yaml", "expected_flat.txt"),
        ("file1.json", "file2.yml", "expected_flat.txt"),
    ],
)
def test_generate_diff_flat(first, second, expected):
    result = generate_diff(TEST_DATA / first, TEST_DATA / second)
    assert result == read_expected(expected)


def test_identical_files_have_no_signs():
    result = generate_diff(TEST_DATA / "file1.json", TEST_DATA / "file1.json")
    assert "+" not in result
    assert "-" not in result


def test_empty_files():
    path = TEST_DATA / "empty.json"
    assert generate_diff(path, path) == "{\n}"


def test_null_value_is_printed_as_null(tmp_path):
    first = tmp_path / "a.json"
    second = tmp_path / "b.json"
    first.write_text(json.dumps({"key": None}))
    second.write_text(json.dumps({"key": 1}))
    assert generate_diff(first, second) == "{\n  - key: null\n  + key: 1\n}"