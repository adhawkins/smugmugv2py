from iso8601 import parse_date

class AlbumImage(object):
	def __init__(self, image):
		if "Image" in image["Uris"]:
			self.uri = image["Uris"]["Image"]
		else:
			self.uri = image["Uri"]

		self.title = image["Title"]
		self.caption = image["Caption"]
		self.keywords = image["Keywords"]
		self.filename = image["FileName"]
		self.archived_size = image["ArchivedSize"]
		self.last_updated = parse_date(image["LastUpdated"]).replace(tzinfo=None)

	@classmethod
	def get_album_image(cls, connection, image_uri):
		return cls(connection.get(image_uri)["Image"])

	def delete_album_image(self, connection):
		return connection.delete(self.uri)

	def change_album_image(self, connection, changes):
		return AlbumImage(connection.patch(self.uri, changes)["Response"]["Image"])
