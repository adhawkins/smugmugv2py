class AlbumImage:
	def __init__(self, image):
		self.uri = image["Uri"]
		self.title = image["Title"]
		self.caption = image["Caption"]
		self.keywords = image["Keywords"]
		self.filename = image["FileName"]

	def delete_album_image(self, connection):
		return connection.delete(self.uri)

	def change_album_image(self, connection, changes):
		return connection.patch(self.uri, changes)["Response"]["AlbumImage"]
