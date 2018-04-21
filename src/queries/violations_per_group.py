"""This module provides the query to retrieve the number of violations per group."""


def initialize_violations_per_group(guidelines, violations_per_group):
    """Initialize the violations to 0 for all groups"""

    for key in guidelines:
        group = guidelines[key].get_group()
        if group not in violations_per_group.keys():
            violations_per_group[group] = 0


def count_violations_per_group(guideline_violations, violations_per_group):
    """Count the number of violations per group"""

    for guideline_violation in guideline_violations:
        guideline = guideline_violation[0]

        group = guideline.get_group()
        if group in violations_per_group.keys():
            violations_per_group[group] += 1
        else:
            violations_per_group[group] = 1


def get_violations_per_group(guideline_violations, guidelines):
    """ Get the number of violations per group """

    violations_per_group = {}

    if any(guidelines):
        initialize_violations_per_group(guidelines, violations_per_group)
        count_violations_per_group(guideline_violations, violations_per_group)

    return violations_per_group
