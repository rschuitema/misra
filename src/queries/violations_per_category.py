"""This module provides the query to retrieve the number of violations per category."""


def get_violations_per_category(guideline_violations, guidelines):
    """ Get the number of violations per category """

    violations_per_category = {}
    if any(guidelines):

        # initialize the violations to 0 for all categories
        violations_per_category = {"Required": 0, "Advisory": 0, "Mandatory": 0}

        # count all violations per category
        for guideline_violation in guideline_violations:
            guideline = guideline_violation[0]

            category = guideline.get_category()
            if category in violations_per_category.keys():
                violations_per_category[category] += 1
            else:
                violations_per_category[category] = 1

    return violations_per_category
