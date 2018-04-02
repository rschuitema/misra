""" This module contains all functions to write misra violation reports to a file """

import csv
import operator

# custom compare function to compare the rules
from src.writers.misra_compare_rule import determine_compare_method


def save_violations_per_rule(violations_per_rule, guidelines, standard):
    """ Save the violations per rule to a file """

    method = determine_compare_method(standard)
    sorted_violations = sorted(violations_per_rule, key=method)

    outputfile = "misra-" + standard + "-violations-per-rule.csv"

    with open(outputfile, 'w') as output:
        csvwriter = csv.writer(output, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['Rule', 'Violations', 'Description'])

        for key in sorted_violations:

            if key in guidelines.keys():
                csvwriter.writerow([key,
                                    violations_per_rule[key],
                                    guidelines[key].get_description()])


def save_violations_per_category(violations_per_category, standard):
    """ Save the violations per category to a file """

    outputfile = "misra-" + standard + "-violations-per-category.csv"

    with open(outputfile, 'w') as output:
        csvwriter = csv.writer(output, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['Category', 'Violations'])

        for key in violations_per_category:
            csvwriter.writerow([key,
                                violations_per_category[key]])


def save_violations_per_group(violations_per_group, standard):
    """ Save the violations per group to a file """

    outputfile = "misra-" + standard + "-violations-per-group.csv"

    with open(outputfile, 'w') as output:
        csvwriter = csv.writer(output, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['Group', 'Violations'])

        for key in violations_per_group:
            csvwriter.writerow([key, violations_per_group[key]])


def save_violations_per_file(violations_per_file, standard):
    """ Save the violations per file to a file """

    sorted_violations = sorted(violations_per_file.items(), key=operator.itemgetter(1), reverse=True)

    outputfile = "misra-" + standard + "-violations-per-file.csv"

    with open(outputfile, 'w') as output:
        csvwriter = csv.writer(output, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['File', 'Violations'])

        for key in sorted_violations:
            csvwriter.writerow([key[0], int(key[1])])
