""" This module contains all functions to write misra violation reports to console output """

import operator
from src.writers.misra_compare_rule import determine_compare_method


def print_violations_per_rule(violations_per_rule, standard):
    """ Print the violations per rule on the standard output """

    method = determine_compare_method(standard)
    sorted_violations = sorted(violations_per_rule, key=method)

    print("-----------")
    for key in sorted_violations:
        print('%s,%s' % (key, violations_per_rule[key]))


def print_violations_per_category(violations_per_category):
    """ Print the violations per category on the standard output """

    print("-----------")
    for key in violations_per_category:
        print('%s,%s' % (key, violations_per_category[key]))


def print_violations_per_group(violations_per_group):
    """ Print the violations per group on the standard output """

    print("-----------")
    for key in violations_per_group:
        print('%s,%s' % (key, violations_per_group[key]))


def print_violations_per_file(violations_per_file):
    """ Print the violations per file on the standard output """

    sorted_violations = sorted(violations_per_file.items(), key=operator.itemgetter(1), reverse=True)

    print("-----------")
    for key in sorted_violations:
        print('%s,%s' % (key[0], key[1]))
