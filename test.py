#!/usr/bin/python

from smugmugv2py import Connection, User, SmugMugv2Exception, Node, Album
from sys import stdout, stdin
from os import linesep, path
from pprint import pprint
from test_setup import api_key, api_secret, token, secret

def do_indent(indent):
	for x in range(0, indent):
		stdout.write(" ")

def print_album(node, indent):
	album = Album.get_album(connection, node["Uris"]["Album"])
	stdout.write(", " + str(album["ImageCount"]) + " images")

def print_node(node, indent):
	do_indent(indent)
	stdout.write("'" + node["Name"] + "' (" + node["Type"] + ") - " + node["Privacy"])
	if node["Type"]=="Album":
		print_album(node, indent)
	print
	if node["HasChildren"]:
		children=Node.get_node_children(connection, node)
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
	nodeUri=User.get_authorized_user(connection)["Uris"]["Node"]
	node = Node.get_node(connection, nodeUri)
	print_node(node, 0)

	pprint(connection.upload_image("focuszetec.jpeg", "/api/v2/album/25cj3F"))

except SmugMugv2Exception as e:
	print "Error: " + str(e)

