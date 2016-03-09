from smugmugv2py import Connection

class User(object):
	def __init__(self, json):
		self.nickname = json["NickName"]
		self.name = json["Name"]
		self.node = json["Uris"]["Node"]

	@classmethod
	def get_authorized_user(cls, connection):
		return cls(connection.get(Connection.BASE_URL+'!authuser')["User"])

	@classmethod
	def get_specific_user(cls, connection, user):
		return cls(connection.get(Connection.BASE_URL+"/user/" + user)["User"])
