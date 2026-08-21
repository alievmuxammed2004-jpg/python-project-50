import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="Path to the first configuration file")
    parser.add_argument("second_file", help="Path to the second configuration file")

    # Флаг -h / --help создаётся автоматически, явно добавлять не нужно

    args = parser.parse_args()
    # Здесь позже будет логика сравнения файлов
    # print("Comparing:", args.first_file, "and", args.second_file)

if __name__ == "__main__":
    main()
