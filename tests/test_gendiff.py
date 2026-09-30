from pathlib import Path

from gendiff import generate_diff

FIXTURES = Path(__file__).parent / "fixtures"


def test_generate_diff_flat_json():
    expected = (FIXTURES / "expected_flat.txt").read_text().strip()
    result = generate_diff(
        FIXTURES / "file1.json",
        FIXTURES / "file2.json",
    )
    assert result == expected