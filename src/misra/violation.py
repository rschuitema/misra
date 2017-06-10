class Violation:

    def __init__(self, file, line, column, guideline, entity):
        self.file = file
        self.line = line
        self.column = column
        self.guideline = guideline
        self.entity = entity

    def set_file(self, file):
        self.file = file
        
    def get_file(self):
        return self.file
        
    def set_line(self, line):
        self.line = line
        
    def get_line(self):
        return self.line

    def set_column(self, column):
        self.column = column
        
    def get_column(self):
        return self.column

    def set_entity(self, entity):
        self.entity = entity
        
    def get_entity(self):
        return self.entity

    def set_guideline(self, guideline):
        self.guideline = guideline
        
    def get_guideline(self):
        return self.guideline

