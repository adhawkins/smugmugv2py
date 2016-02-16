def get_node(connection, node_uri):
	return connection.get(node_uri)["Node"];

def get_node_children(connection, node):
	return connection.get(node["Uris"]["ChildNodes"])["Node"];

