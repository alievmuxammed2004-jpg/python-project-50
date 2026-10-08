from gendiff.formatters.stylish import format_stylish

FORMATTERS = {
    "stylish": format_stylish,
}


def get_formatter(format_name):
    if format_name not in FORMATTERS:
        raise ValueError(f"Unknown format: {format_name}")
    return FORMATTERS[format_name]