from AlbumImage import AlbumImage

class Album:
	def __init__(self, album):
		self.uri = album["Uri"]
		self.name = album["Name"]
		self.url_name = album["UrlName"]
		self.nice_name = album["NiceName"]
		self.description = album["Description"]
		self.image_count = album["ImageCount"]
		if self.image_count:
			self.__images = album["Uris"]["AlbumImages"]

	def get_images(self, connection):
		ret=[]

		if self.image_count:
			images = connection.get(self.__images)["AlbumImage"]
			for image in images:
				thisimage = AlbumImage(image)
				ret.append(thisimage)

		return ret

