def format_value(value):
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def format_node(node):
    key = node["key"]
    node_type = node["type"]
    if node_type == "changed":
        return [
            f"  - {key}: {format_value(node['old_value'])}",
            f"  + {key}: {format_value(node['new_value'])}",
        ]
    signs = {"added": "+", "removed": "-", "unchanged": " "}
    return [f"  {signs[node_type]} {key}: {format_value(node['value'])}"]


def format_stylish(diff):
    lines = [line for node in diff for line in format_node(node)]
    return "\n".join(["{", *lines, "}"])