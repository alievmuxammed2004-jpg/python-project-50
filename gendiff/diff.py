def make_node(key, data1, data2):
    if key not in data2:
        return {"key": key, "type": "removed", "value": data1[key]}
    if key not in data1:
        return {"key": key, "type": "added", "value": data2[key]}
    old, new = data1[key], data2[key]
    if isinstance(old, dict) and isinstance(new, dict):
        return {
            "key": key,
            "type": "nested",
            "children": build_diff(old, new),
        }
    if old == new:
        return {"key": key, "type": "unchanged", "value": old}
    return {
        "key": key,
        "type": "changed",
        "old_value": old,
        "new_value": new,
    }


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    return [make_node(key, data1, data2) for key in keys]