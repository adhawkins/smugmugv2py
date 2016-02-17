class Node:
	def __init__(self, node):
		self.uri = node["Uri"]
		self.name = node["Name"]
		self.type = node["Type"]
		self.privacy = node["Privacy"]
		self.has_children = node["HasChildren"]
		if self.has_children:
			self.child_nodes = node["Uris"]["ChildNodes"]

		if self.type == "Album":
			self.album = node["Uris"]["Album"]

	def get_children(self, connection):
		ret=[]

		nodes = connection.get(self.child_nodes)["Node"]
		for node in nodes:
			thisnode = Node(node)
			ret.append(thisnode)

		return ret

