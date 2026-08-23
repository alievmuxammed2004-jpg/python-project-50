import json


def parse_file(filepath):
    """Читает файл по указанному пути и возвращает данные в виде словаря."""
    with open(filepath) as f:
        data = json.load(f)
    return data


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    # Пока просто возвращаем данные — сравнение будет реализовано позже
    return data1, data2