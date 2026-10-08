from gendiff.diff import build_diff


def test_build_diff_structure():
    first = {"a": 1, "b": {"c": 1}, "d": 1}
    second = {"a": 2, "b": {"c": 1, "e": 2}, "f": 3}
    assert build_diff(first, second) == [
        {"key": "a", "type": "changed", "old_value": 1, "new_value": 2},
        {
            "key": "b",
            "type": "nested",
            "children": [
                {"key": "c", "type": "unchanged", "value": 1},
                {"key": "e", "type": "added", "value": 2},
            ],
        },
        {"key": "d", "type": "removed", "value": 1},
        {"key": "f", "type": "added", "value": 3},
    ]


def test_dict_replaced_by_scalar_is_changed():
    result = build_diff({"a": {"b": 1}}, {"a": "str"})
    assert result == [
        {
            "key": "a",
            "type": "changed",
            "old_value": {"b": 1},
            "new_value": "str",
        },
    ]