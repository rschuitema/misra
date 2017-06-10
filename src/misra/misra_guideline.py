class MisraGuideline:

	def __init__(self, id, classification, category, group, description):
		self.id = id
		self.classification = classification
		self.category = category
		self.group = group
		self.description = description
		self.count = 0

	def getId(self):
		return self.id
		
	def getClassification(self):
		return self.classification
		
	def getCategory(self):
		return self.category

	def getGroup(self):
		return self.group
		
	def getDescription(self):
		return self.description