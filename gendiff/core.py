from gendiff.diff import build_diff
from gendiff.formatters import get_formatter
from gendiff.parser import parse_file


def generate_diff(file_path1, file_path2, format_name="stylish"):
    formatter = get_formatter(format_name)
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    return formatter(build_diff(data1, data2))