from gendiff.formatters.stylish import format_stylish
from gendiff.parser import parse_file


def make_node(key, data1, data2):
    if key not in data2:
        return {"key": key, "type": "removed", "value": data1[key]}
    if key not in data1:
        return {"key": key, "type": "added", "value": data2[key]}
    if data1[key] == data2[key]:
        return {"key": key, "type": "unchanged", "value": data1[key]}
    return {
        "key": key,
        "type": "changed",
        "old_value": data1[key],
        "new_value": data2[key],
    }


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    return [make_node(key, data1, data2) for key in keys]


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    return format_stylish(build_diff(data1, data2))