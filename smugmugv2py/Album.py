class Album:
	def __init__(self, album):
		self.uri = album["Uri"]
		self.name = album["Name"]
		self.nice_name = album["NiceName"]
		self.description = album["Description"]
		self.image_count = album["ImageCount"]
