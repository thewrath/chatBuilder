#!/usr/bin/env python
# coding: utf-8

import socket

from server.configuration import *
from server.clientThread import *
from server.database import *

import threading

"""
	Server module
	======================
"""

class Server(threading.Thread):

	def __init__(self, configFile, section):

		"""
		Constructor of Server.

		This initalise a new Server
		:rtype: void
		"""
		threading.Thread.__init__(self)
		self.config = Configuration(configFile, section)
		self.tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.tcpsock.bind(("",int(float(self.config.get("port")))))

	def run(self):

		"""
		Start method.

		Use for start the server to listen to a specific socket

		:param socketNumber: number of the socket
		:rtype: void

		"""

		while True:
			self.tcpsock.listen(int(float(self.config.get("socketNumber"))))
			print("En écoute...")
			print(self.tcpsock.getsockname())
			(clientsocket, (ip, port)) = self.tcpsock.accept()
			newthread = ClientThread(ip, port, clientsocket, Database(self.config.get("dbIP"),self.config.get("dbUser"),self.config.get("dbPassword"),self.config.get("dbName")))
			newthread.start()


