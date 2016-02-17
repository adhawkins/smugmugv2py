class AlbumImage:
	def __init__(self, image):
		self.uri = image["Uri"]
		self.title = image["Title"]
		self.caption = image["Caption"]
		self.keywords = image["Keywords"]
		self.filename = image["FileName"]
		
