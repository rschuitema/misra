"""This module provides the query to retrieve the number of violations per rule."""


def get_violations_per_rule(guideline_violations, guidelines):
    """ Get the number of violations per rule """

    violations_per_rule = {}

    if any(guidelines):
        initialize_violations_per_rule(guidelines, violations_per_rule)
        count_violations_per_rule(guideline_violations, violations_per_rule)

    return violations_per_rule


def initialize_violations_per_rule(guidelines, violations_per_rule):
    """Initialize the violations to 0 for all rules """

    for rule in guidelines:
        violations_per_rule[rule] = 0


def count_violations_per_rule(guideline_violations, violations_per_rule):
    """Count all violations per rule"""

    for guideline_violation in guideline_violations:
        guideline = guideline_violation[0]

        rule = guideline.get_id()
        if rule in violations_per_rule.keys():
            violations_per_rule[rule] += 1
        else:
            violations_per_rule[rule] = 1
