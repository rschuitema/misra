import csv
import re

from misra_guideline import MisraGuideline
from violation import Violation

class MisraParser:

    def __init__(self):
        self.guidelines = {}
        self.violations = []

    def getGuidelines(self):
        return self.guidelines

    def getViolations(self):
        return self.violations

    def readGuidelines(self, guidelineFile):
        with open(guidelineFile, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=',' , quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            next(reader, None)  # skip the headers
            for row in reader:
                rule = row[0]
                classification = row[1]
                category = row[2]
                group = row[3]
                description = row[4]
                if rule not in self.guidelines.keys():
                    self.guidelines[rule] = MisraGuideline(rule, classification, category, group, description)


    def readViolations(self, violationsFile):
        with open(violationsFile, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader, None)  # skip the headers
            for row in reader:
                if row:
                    file = row[0]
                    dummy = row[1]
                    linenr = row[2]
                    column = row[3]

                    result = re.search ('([0-9]+\.[0-9]+)', str(row[4]))
                    guideline = None
                    if result:
                        rule = result.group (1)
                        if rule in self.guidelines.keys():
                            guideline = self.guidelines[rule]
                        else:
                            guideline = MisraGuideline(rule, "Unknown", "Unknown", "Unknown", "Unknown")

                    entity = row[5]

                    self.violations.append(Violation(file, linenr, column, guideline, entity))


    def violationsPerRule(self):

        violationsPerRule = {}

        # initialize the violations to 0 for all rules
        for rule in self.guidelines:
            violationsPerRule[rule] = 0

        # count all violations per rule
        for violation in self.violations :
            rule = violation.get_guideline().get_id()
            if rule in violationsPerRule.keys():
                violationsPerRule[rule] += 1
            else:
                violationsPerRule[rule] = 1

        return violationsPerRule

    def violationsPerCategory(self):

        violationsPerCategory = {}

        # initialize the violations to 0 for all categories
        violationsPerCategory["Required"] = 0
        violationsPerCategory["Advisory"] = 0
        violationsPerCategory["Mandatory"] = 0

        # count all violations per category
        for violation in self.violations :
            category = violation.get_guideline().get_category()
            if category in violationsPerCategory.keys():
                violationsPerCategory[category] += 1
            else:
                violationsPerCategory[category] = 1

        return violationsPerCategory

    def violationsPerGroup(self):

        violationsPerGroup = {}

        # initialize the violations to 0 for all groups
        for key in self.guidelines:
            group = self.guidelines[key].get_group()
            if group not in violationsPerGroup.keys():
                violationsPerGroup[group] = 0

        # count all violations per group
        for violation in self.violations :
            group = violation.get_guideline().get_group()
            if group in violationsPerGroup.keys():
                violationsPerGroup[group] += 1
            else:
                violationsPerGroup[group] = 1

        return violationsPerGroup

    def violationsPerFile(self):

        violationsPerFile = {}

        # initialize the violations to 0 for all groups
        for violation in self.violations:
            file = violation.get_file()
            if file not in violationsPerFile.keys():
                violationsPerFile[file] = 0

        # count all violations per file
        for violation in self.violations :
            file = violation.get_file()
            if file in violationsPerFile.keys():
                violationsPerFile[file] += 1
            else:
                violationsPerFile[file] = 1

        return violationsPerFile
