"""This module provides the query to retrieve the number of violations per file."""


def initialize_violations_per_file(guideline_violations, violations_per_file):
    """Initialize the violations to 0 for all files"""

    for guideline_violation in guideline_violations:
        file = guideline_violation[1]
        violations_per_file[file] = 0


def count_violations_per_file(guideline_violations, violations_per_file):
    """Count the number of violations per group"""

    for guideline_violation in guideline_violations:
        file = guideline_violation[1]

        if file in violations_per_file.keys():
            violations_per_file[file] += 1
        else:
            violations_per_file[file] = 1


def get_violations_per_file(guideline_violations, guidelines):
    """ Get the number of violations per file """

    violations_per_file = {}

    if any(guidelines):
        initialize_violations_per_file(guideline_violations, violations_per_file)
        count_violations_per_file(guideline_violations, violations_per_file)

    return violations_per_file
