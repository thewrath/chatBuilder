#!/usr/bin/env python
# coding: utf-8

import socket
from clientThread import *
from database import *

"""
	Server module
	======================
"""

class Server():

	def __init__(self):

		"""
		Constructor of Server.

		This initalise a new Server
		:rtype: void
		"""

		self.tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.tcpsock.bind(("",1111))

	def start(self, socketNumber):

		"""
		Start method.

		Use for start the server to listen to a specific socket

		:param socketNumber: number of the socket
		:rtype: void

		"""

		while True:
			self.tcpsock.listen(socketNumber)
			print("En écoute...")
			print(self.tcpsock.getsockname())
			(clientsocket, (ip, port)) = self.tcpsock.accept()
			newthread = ClientThread(ip, port, clientsocket, Database("localhost","root","root","chatAppDB"))
			newthread.start()


