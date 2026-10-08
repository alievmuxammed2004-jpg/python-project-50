INDENT = 4
SIGNS = {"added": "+", "removed": "-", "unchanged": " "}


def format_value(value, depth):
    if isinstance(value, dict):
        lines = [
            make_line(depth + 1, " ", key, item)
            for key, item in value.items()
        ]
        closing = " " * (depth * INDENT) + "}"
        return "\n".join(["{", *lines, closing])
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def make_line(depth, sign, key, value):
    indent = " " * (depth * INDENT - 2)
    return f"{indent}{sign} {key}: {format_value(value, depth)}"


def render_node(node, depth):
    key = node["key"]
    kind = node["type"]
    if kind == "nested":
        indent = " " * (depth * INDENT)
        children = render(node["children"], depth + 1)
        return [f"{indent}{key}: {{", *children, f"{indent}}}"]
    if kind == "changed":
        return [
            make_line(depth, "-", key, node["old_value"]),
            make_line(depth, "+", key, node["new_value"]),
        ]
    return [make_line(depth, SIGNS[kind], key, node["value"])]


def render(diff, depth):
    return [line for node in diff for line in render_node(node, depth)]


def format_stylish(diff):
    return "\n".join(["{", *render(diff, 1), "}"])