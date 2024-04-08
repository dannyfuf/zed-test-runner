import argparse

from commands import run_command, get_test_command
from patterns import find_test_case_rows, get_test_case_row, get_test_case_description

def main(root, current_file_path, cursor_row_number):
    with open(current_file_path, 'r') as file:
        lines = file.readlines()
        test_case_rows = find_test_case_rows(lines)

    test_case_row = get_test_case_row(test_case_rows, cursor_row_number)
    test_case_description = get_test_case_description(lines[test_case_row])
    test_command = get_test_command(root, current_file_path, test_case_description)
    return run_command(test_command)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('root', type=str)
    parser.add_argument('file_path', type=str)
    parser.add_argument('row_number', type=int)
    args = parser.parse_args()
    main(args.root, args.file_path, args.row_number)
