""" This module represents the data of a MISRA guideline """


class MisraGuideline:
    """ Representation of the MISRA guideline """

    def __init__(self, guide):
        """ Construct and initialize the guideline """

        self.identifier = guide[0]
        self.classification = guide[1]
        self.category = guide[2]
        self.group = guide[3]
        self.description = guide[4]
        self.count = 0

    def get_id(self):
        """ Get the identifier of the guideline """

        return self.identifier

    def get_classification(self):
        """ Get the classification of the guideline """

        return self.classification

    def get_category(self):
        """ Get the category of the guideline """

        return self.category

    def get_group(self):
        """ Get the group of the guideline """

        return self.group

    def get_description(self):
        """ Get the description of the guideline """

        return self.description
