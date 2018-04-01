""" Parse misra violations in a log file and present the violations in several views """

import csv
import re

from misra_guideline import MisraGuideline
from violation import Violation


class MisraParser:
    """ Parse misra violations in a log file and present the violations in several views """

    def __init__(self):
        """ Construct the misra parser """

        self.guidelines = {}
        self.violations = []

    def get_guidelines(self):
        """ Get the guidelines """

        return self.guidelines

    def get_violations(self):
        """ Get the violations """

        return self.violations

    def read_guidelines(self, guideline_file):
        """ Read the guidlines from a CSV file """

        with open(guideline_file, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            next(reader, None)  # skip the headers
            for row in reader:
                rule = row[0]
                classification = row[1]
                category = row[2]
                group = row[3]
                description = row[4]
                if rule not in self.guidelines.keys():
                    self.guidelines[rule] = MisraGuideline((rule, classification, category, group, description))

    def read_violations(self, violations_file):
        """ Read the violations from a CSV file """

        with open(violations_file, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader, None)  # skip the headers
            for row in reader:
                if row:
                    file = row[0]
                    dummy = row[1]
                    linenr = row[2]
                    column = row[3]

                    result = re.search('([0-9]+.[0-9]+)', str(row[4]))
                    guideline = None
                    if result:
                        rule = result.group(1)
                        if rule in self.guidelines.keys():
                            guideline = self.guidelines[rule]
                        else:
                            guideline = MisraGuideline((rule, "Unknown", "Unknown", "Unknown", "Unknown"))

                    entity = row[5]

                    self.violations.append(Violation(file, linenr, column, guideline, entity))

    def violations_per_rule(self):
        """ Get the number of violations per rule """

        violations_per_rule = {}

        # initialize the violations to 0 for all rules
        for rule in self.guidelines:
            violations_per_rule[rule] = 0

        # count all violations per rule
        for violation in self.violations:
            rule = violation.get_guideline().get_id()
            if rule in violations_per_rule.keys():
                violations_per_rule[rule] += 1
            else:
                violations_per_rule[rule] = 1

        return violations_per_rule

    def violations_per_category(self):
        """ Get the number of violations per category """

        # initialize the violations to 0 for all categories
        violations_per_category = {"Required": 0, "Advisory": 0, "Mandatory": 0}

        # count all violations per category
        for violation in self.violations:
            category = violation.get_guideline().get_category()
            if category in violations_per_category.keys():
                violations_per_category[category] += 1
            else:
                violations_per_category[category] = 1

        return violations_per_category

    def violations_per_group(self):
        """ Get the number of violations per group """

        violations_per_group = {}

        # initialize the violations to 0 for all groups
        for key in self.guidelines:
            group = self.guidelines[key].get_group()
            if group not in violations_per_group.keys():
                violations_per_group[group] = 0

        # count all violations per group
        for violation in self.violations:
            group = violation.get_guideline().get_group()
            if group in violations_per_group.keys():
                violations_per_group[group] += 1
            else:
                violations_per_group[group] = 1

        return violations_per_group

    def violations_per_file(self):
        """ Get the number of violations per file """

        violations_per_file = {}

        # initialize the violations to 0 for all groups
        for violation in self.violations:
            file = violation.get_file()
            if file not in violations_per_file.keys():
                violations_per_file[file] = 0

        # count all violations per file
        for violation in self.violations:
            file = violation.get_file()
            if file in violations_per_file.keys():
                violations_per_file[file] += 1
            else:
                violations_per_file[file] = 1

        return violations_per_file
