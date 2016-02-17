from smugmugv2py import Connection

class User:
	def __init__(self, json):
		self.nickname = json["NickName"]
		self.name = json["Name"]
		self.node = json["Uris"]["Node"]
		
