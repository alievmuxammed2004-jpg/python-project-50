def format_value(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def render_node(node, path):
    name = f"{path}.{node['key']}" if path else node["key"]
    kind = node["type"]
    if kind == "nested":
        return render(node["children"], name)
    if kind == "added":
        value = format_value(node["value"])
        return [f"Property '{name}' was added with value: {value}"]
    if kind == "removed":
        return [f"Property '{name}' was removed"]
    if kind == "changed":
        old = format_value(node["old_value"])
        new = format_value(node["new_value"])
        return [f"Property '{name}' was updated. From {old} to {new}"]
    return []


def render(diff, path=""):
    return [line for node in diff for line in render_node(node, path)]


def format_plain(diff):
    return "\n".join(render(diff))