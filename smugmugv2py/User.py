from smugmugv2py import Connection

def get_authorized_user(connection):
	return connection.make_request(Connection.BASE_URL+'!authuser')["User"];

def get_specific_user(connection, user):
	return connection.make_request(Connection.BASE_URL+"/user/" + user)["User"];
