""" Reads the misra guidelines from a csv file """

import csv
import re
from src.misra.misra_guideline import MisraGuideline


def is_valid_classification(classification):
    """ Check if the classification is a MISRA defined classification """

    allowed_classifications = ['Rule']

    return classification in allowed_classifications


def is_valid_category(category):
    """ Check if the category is a MISRA defined category """

    allowed_categories = ['Required', 'Advisory', 'Mandatory']

    return category in allowed_categories


def is_valid_group(group):
    """ Check if the group is a MISRA defined group """

    allowed_groups = ['Environment',
                      'Language extensions',
                      'Documentations',
                      'Character sets',
                      'Identifiers',
                      'Types',
                      'Constants',
                      'Declarations and definitions',
                      'Initialization',
                      'Arithmetic type conversions',
                      'Pointer type conversions',
                      'Expressions',
                      'Control statement expressions',
                      'Control flow',
                      'Switch statements',
                      'Functions',
                      'Pointers and arrays',
                      'Structures and unions',
                      'Preprocessing directives',
                      'Standard libraries',
                      'Run-time failures']

    return group in allowed_groups


def is_valid_rule(rule):
    """ Check if format of the rule is valid """

    return re.search(r'([0-9]+\.[0-9]+)', str(rule))


def is_valid_guideline(guide):
    """ Check if the guideline is valid """

    rule, classification, category, group, description = guide
    if not is_valid_rule(rule):
        return False

    if not is_valid_classification(classification):
        return False

    if not is_valid_category(category):
        return False

    if not is_valid_group(group):
        return False

    return True


def get_standard_file(standard):
    """ Map the standard to a file """

    standard_files = {"C2004": "misra-c2004-guidelines.csv",
                      "C2012": "misra-c2012-guidelines.csv",
                      "CPP2008": "misra-cpp2008-guidelines.csv"}

    if standard in standard_files.keys():
        return standard_files[standard]

    return None


def store_guideline(guideline, guidelines):
    """ Store the guideline in the dictionary if it is a new one"""

    if guideline[0] not in guidelines.keys():
        guidelines[guideline[0]] = MisraGuideline(guideline)


def read_guidelines(standard_file, csv_reader=None):
    """ Read the guidelines form a CSV file"""

    guidelines = {}

    with open(standard_file, 'rt') as csv_file:
        if csv_reader is None:
            csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"',
                                        quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in csv_reader:
            guideline = (row['Rule'], row['Classification'], row['Category'], row['Group'], row['Description'])
            if is_valid_guideline(guideline):
                store_guideline(guideline, guidelines)
            else:
                print("Incorrect format of guideline: {}".format(guideline))

    return guidelines


def read_misra_guidelines(standard, csv_reader=None):
    """ Read the MISRA guidelines indicated by <standard> from a CSV file """

    guidelines = {}

    standard_file = get_standard_file(standard)
    if standard_file is not None:
        guidelines = read_guidelines(standard_file, csv_reader)

    return guidelines
