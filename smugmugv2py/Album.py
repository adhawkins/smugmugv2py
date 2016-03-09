from AlbumImage import AlbumImage

class Album(object):
	def __init__(self, album):
		self.uri = album["Uri"]
		self.name = album["Name"]
		self.url_name = album["UrlName"]
		self.description = album["Description"]
		self.image_count = album["ImageCount"]
		self.keywords = album["Keywords"]
		self.sort_method = album["SortMethod"]
		self.sort_direction = album["SortDirection"]
		if self.image_count:
			self.__images = album["Uris"]["AlbumImages"]

	@classmethod
	def get_album(cls, connection, album_uri):
		return cls(connection.get(album_uri)["Album"])

	def get_images(self, connection):
		ret=[]

		if self.image_count:
			images = connection.get(self.__images)["AlbumImage"]
			for image in images:
				thisimage = AlbumImage(image)
				ret.append(thisimage)

		return ret

	def delete_album(self, connection):
		return connection.delete(self.uri)

	def change_album(self, connection, changes):
		return connection.patch(self.uri, changes)["Response"]["Album"]
