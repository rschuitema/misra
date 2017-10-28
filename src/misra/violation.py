""" This module represents a violation against a MISRA guideline """

class Violation:
    """ Represents a violation against a MISRA guideline """

    def __init__(self, file, line, column, guideline, entity):
        """ Construct a violation """

        self.file = file
        self.line = line
        self.column = column
        self.guideline = guideline
        self.entity = entity

    def set_file(self, file):
        """ Set the file in which the violation ocurred """

        self.file = file

    def get_file(self):
        """ Get the file in which the violation ocurred """

        return self.file

    def set_line(self, line):
        """ Set the line number in which the violation ocurred """

        self.line = line

    def get_line(self):
        """ Get the line number in which the violation ocurred """

        return self.line

    def set_column(self, column):
        """ Set the column number of the line in which the violation ocurred """

        self.column = column

    def get_column(self):
        """ Get the column number of the line in which the violation ocurred """

        return self.column

    def set_entity(self, entity):
        """ Set the entity in which violated the guideline """

        self.entity = entity

    def get_entity(self):
        """ Get the entity in which violated the guideline """

        return self.entity

    def set_guideline(self, guideline):
        """ Set the guideline that is violated """

        self.guideline = guideline

    def get_guideline(self):
        """ Get the guideline that is violated """

        return self.guideline
