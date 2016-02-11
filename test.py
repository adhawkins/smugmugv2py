#!/usr/bin/python

from smugmugv2py import Connection, User, SmugMugv2Exception, Node
from sys import stdout, stdin
from os import linesep
from pprint import pprint
from test_setup import api_key, api_secret, token, secret

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
	children=Node.get_node_children(connection, nodeUri)
	for child in children:
		print "Found child: " + child["Name"] + ", type: " + child["Type"]
except SmugMugv2Exception as e:
	print "Error: " + str(e)

