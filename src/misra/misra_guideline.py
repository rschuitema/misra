class MisraGuideline:

	def __init__(self, id, classification, category, group, description):
		self.id = id
		self.classification = classification
		self.category = category
		self.group = group
		self.description = description
		self.count = 0

	def get_id(self):
		return self.id
		
	def get_classification(self):
		return self.classification
		
	def get_category(self):
		return self.category

	def get_group(self):
		return self.group
		
	def get_description(self):
		return self.description