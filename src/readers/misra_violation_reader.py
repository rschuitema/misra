""" Read the misra violations from a log file """
import csv
import re


def is_valid_line(line):
    """Check if the line is formatted correctly"""

    return re.search(r'([0-9]+)', str(line))


def is_valid_column(column):
    """Check if the column is formatted correctly"""

    return re.search(r'([0-9]+)', str(column))


def is_valid_check(check):
    """Check if the check is formatted correctly"""

    return re.search(r'^([0-9]+\.[0-9]+)', check)


def is_valid_file(file):
    """Check if file is formatted correctly"""

    return isinstance(file, str)


def is_valid_entity(entity):
    """Check if entity if formatted correctly"""

    return isinstance(entity, str)


def is_valid_misra_violation(misra_violation):
    """Check if misra violation is formatted correctly"""

    return isinstance(misra_violation, str)


def is_valid_violation(violation):
    """ Check if the violation is formatted correctly """

    file, misra_violation, line, column, check, entity = violation

    valid = is_valid_line(line)
    if valid:
        valid = is_valid_column(column)

    if valid:
        valid = is_valid_check(check)

    if valid:
        valid = is_valid_file(file)

    if valid:
        valid = is_valid_misra_violation(misra_violation)

    if valid:
        valid = is_valid_entity(entity)

    return valid


def store_violations(violation, violations):
    """ Store the violations in the list """

    violations.append(violation)


def read_violations(violation_file, csv_reader=None):
    """ Read the violations from csv file """

    violations = []

    with open(violation_file, 'rt') as csv_file:
        if csv_reader is None:
            csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"',
                                        quoting=csv.QUOTE_ALL, skipinitialspace=True)

        for row in csv_reader:
            violation = (row['File'], row['Violation'], row['Line'], row['Column'], row['Check'], row['Entity'])
            if is_valid_violation(violation):
                store_violations(violation, violations)
            else:
                print("Incorrect format of violation: {}".format(violation))

    return violations


def read_misra_violations(violation_file, csv_reader=None):
    """ Read violations from csv file """

    violations = []

    if violation_file is not None:
        violations = read_violations(violation_file, csv_reader)

    return violations
