from gendiff.formatters.plain import format_plain


def test_plain_values():
    diff = [
        {"key": "a", "type": "added", "value": 5},
        {"key": "b", "type": "added", "value": [1, 2]},
        {"key": "c", "type": "removed", "value": None},
        {"key": "d", "type": "unchanged", "value": 1},
    ]
    assert format_plain(diff) == "\n".join([
        "Property 'a' was added with value: 5",
        "Property 'b' was added with value: [complex value]",
        "Property 'c' was removed",
    ])