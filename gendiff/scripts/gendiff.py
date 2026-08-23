import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output (stylish, plain, json)'
    )

    args = parser.parse_args()

    result = generate_diff(args.first_file, args.second_file, format=args.format)
    print(result)


if __name__ == '__main__':
    main()