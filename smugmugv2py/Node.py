def get_node(connection, node_uri):
	return connection.make_request(node_uri)["Node"];

def get_node_children(connection, node_uri):
	return connection.make_request(node_uri+"!children")["Node"];

