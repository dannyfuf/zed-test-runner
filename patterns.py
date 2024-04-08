from math import inf
import re

PATTERN = r"(describe|it)(\s*)\((\'|\")([\w\s]+)(\'|\")(\s*),"
REGEX_PATTERN = re.compile(PATTERN)

def find_test_case_rows(lines):
    rows = []
    for i, line in enumerate(lines):
        if REGEX_PATTERN.search(line):
            rows.append(i)
    return rows;

def get_test_case_row(
    test_case_rows,
    row_number
):
    context_row_numbers = test_case_rows
    shortest_distance = inf
    closest_row = 0
    for row in context_row_numbers:
        distance = abs(row - row_number)
        if distance < shortest_distance:
            shortest_distance = distance
            closest_row = row
    return closest_row

def get_test_case_description(line):
    regex = re.compile(PATTERN)
    match = regex.search(line)
    return match.group(4)
