def get_album(connection, album_uri):
	return connection.get(album_uri)["Album"];

