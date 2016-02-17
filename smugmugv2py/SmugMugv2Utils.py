from Connection import Connection

def get_authorized_user(connection):
	return connection.get(Connection.BASE_URL+'!authuser')["User"];

def get_specific_user(connection, user):
	return connection.get(Connection.BASE_URL+"/user/" + user)["User"];

def get_album(connection, album_uri):
	return connection.get(album_uri)["Album"];

def get_node(connection, node_uri):
	return connection.get(node_uri)["Node"];

