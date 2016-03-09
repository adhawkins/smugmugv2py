from Connection import Connection
from User import User
from Node import Node
from Album import Album
from AlbumImage import AlbumImage

__all__ = [
	"Connection",
	"SmugMugv2Exception",
	"User",
	"Node",
	"Album",
	"AlbumImage"
]

class SmugMugv2Exception(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return repr(self.message)

