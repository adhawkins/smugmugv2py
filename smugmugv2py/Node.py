from json import dumps

class Node:
	def __init__(self, node):
		self.uri = node["Uri"]
		self.name = node["Name"]
		self.type = node["Type"]
		self.privacy = node["Privacy"]
		self.has_children = node["HasChildren"]

		if self.type == "Album":
			self.album = node["Uris"]["Album"]
		else:
			self.__child_nodes = node["Uris"]["ChildNodes"]

	def get_children(self, connection):
		ret=[]

		if self.has_children:
			nodes = connection.get(self.__child_nodes)["Node"]
			for node in nodes:
				thisnode = Node(node)
				ret.append(thisnode)

		return ret

	def __create_child_node(self, connection, type, name, url, privacy, description):
		headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
		}

		params = {
			'Type': type,
			'Name': name,
			'UrlName': url.capitalize(),
			'Privacy': privacy,
		}

		if description:
			params['Description']=description
			
		return connection.post(self.child_nodes, data=dumps(params), headers=headers)

	def create_child_folder(self, connection, name, url, privacy, description=None):
		return self.__create_child_node(connection, 'Folder', name, url, privacy, description)

	def create_child_album(self, connection, name, url, privacy, description=None):
		return self.__create_child_node(connection, 'Album', name, url, privacy, description)
