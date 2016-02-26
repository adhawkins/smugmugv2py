#!/usr/bin/python

from smugmugv2py import Connection, User, SmugMugv2Exception, Node, Album, AlbumImage, SmugMugv2Utils
from sys import stdout, stdin
from os import linesep, path
from pprint import pprint
from test_setup import api_key, api_secret, token, secret
from datetime import datetime
from json import dumps
from requests import exceptions

def do_indent(indent):
	for x in range(0, indent):
		stdout.write(" ")

def print_album(node, indent):
	album = Album(SmugMugv2Utils.get_album(connection, node.album))
	stdout.write(", " + str(album.image_count) + " images")
	images = album.get_images(connection)
	for image in images:
		do_indent(indent+1)
		print image.filename + " - " + image.caption

def print_node(node, indent):
	do_indent(indent)
	stdout.write("'" + node.name + "' (" + node.type + ") - " + node.privacy)
	if node.type == "Album":
		print_album(node, indent)
	print
	children=node.get_children(connection)
	for child in children:
		print_node(child, indent+1)

connection = Connection(api_key, api_secret)

if not token or not secret:
	auth_url = connection.get_auth_url(access="Full", permissions="Modify")

	print "Visit the following URL and retrieve a verification code:%s%s" % (linesep, auth_url)

	stdout.write('Enter the six-digit code: ')
	stdout.flush()
	verifier = stdin.readline().strip()

	at, ats = connection.get_access_token(verifier)

	print "Token: " + at
	print "Secret: " + ats

	token = at
	secret = ats

connection.authorise_connection(token, secret)

try:
	user = User.get_authorized_user(connection)
	print "User: " + user.nickname + " (" + user.name + ")"

	node = Node.get_node(connection,user.node)
	#print_node(node, 0)

	#new_node=Node(node.create_child_folder(connection, 'aaaatestnode2','aaaaatestnode2','Public'))
	#print new_node.uri + " - " + new_node.name

	new_node = None

	for thisnode in node.get_children(connection):
		if thisnode.url_name == "Testalbum":
			new_node=thisnode

	if new_node is None:
		new_node=node.create_child_album(connection, 'testalbum','Testalbum','Public', 'A long description for the album')

	print new_node.uri + " - " + new_node.name + new_node.album
	album=Album.get_album(connection, new_node.album)

	try:
		pprint(connection.upload_image('focuszetec.jpeg',
											album.uri))
	except exceptions.ConnectionError as e:
		print "ConnectionError: " + str(e)

		print "Deleting node after failed upload"
		new_node.delete_node(connection)

	#delete_node=Node(node.create_child_folder(connection, 'deletetest','Deletetest','Public'))
	#print "Name: " + delete_node.name + ", url: " + delete_node.url_name
	#pprint(delete_node.delete_node(connection))

	#rename_node=Node(node.create_child_folder(connection, 'renametest','Renametest','Public'))
	#print "Name: " + rename_node.name + ", url: " + rename_node.url_name

	#rename = {
	#	"UrlName": "Renametestchange"
	#}

	#renamed_node=Node(rename_node.change_node(connection, rename))
	#print "Renamed Name: " + renamed_node.name + ", url: " + renamed_node.url_name
	#found_renamed_node=Node(SmugMugv2Utils.get_node(connection, rename_node.uri))
	#print "Found Renamed Name: " + found_renamed_node.name + ", url: " + found_renamed_node.url_name
	#pprint(connection.delete(renamed_node.uri))
except SmugMugv2Exception as e:
	print "Error: " + str(e)

