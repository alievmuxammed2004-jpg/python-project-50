import json
import sys
from pathlib import Path

from gendiff.scripts.gendiff import main

TEST_DATA = Path(__file__).parent / "test_data"


def test_cli_prints_diff(monkeypatch, capsys):
    first = str(TEST_DATA / "file1.json")
    second = str(TEST_DATA / "file2.json")
    monkeypatch.setattr(sys, "argv", ["gendiff", first, second])
    main()
    expected = (TEST_DATA / "expected_flat.txt").read_text().strip()
    assert capsys.readouterr().out.strip() == expected


def test_cli_plain_format(monkeypatch, capsys):
    first = str(TEST_DATA / "nested1.json")
    second = str(TEST_DATA / "nested2.json")
    monkeypatch.setattr(
        sys, "argv", ["gendiff", "--format", "plain", first, second]
    )
    main()
    expected = (TEST_DATA / "expected_nested_plain.txt").read_text()
    assert capsys.readouterr().out.strip() == expected.strip()

def test_cli_json_format(monkeypatch, capsys):
    first = str(TEST_DATA / "nested1.json")
    second = str(TEST_DATA / "nested2.json")
    monkeypatch.setattr(
        sys, "argv", ["gendiff", "--format", "json", first, second]
    )
    main()
    assert isinstance(json.loads(capsys.readouterr().out), list)