#!/usr/bin/env python
# coding: utf-8

import socket
import configparser


"""
	Client module
	======================
"""

class Client:

	def __init__(self):

		self.tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcpsocket.connect(("", 1111))
		self.connected = False
		self.bufLen = 2048

	def receiveData(self):
		receiveData = self.clientsocket.recv(self.bufLen)
		self.sortData(receiveData)
	
	def sendData(self, *datas):
		dataToSend = "&"
		count = len(datas)
		for data in datas:
			count = count - 1
			dataToSend += data
			if not count == 1:
				dataToSend += "&&"
			else:
				dataToSend += "&"
				print(dataToSend)

	def sortData(self, data):
		sortedData = []
		temp = ""
		cut = True
		for c in data:
			if c == '&':
				if cut:
					cut = False
				else:
					cut = True
			else:
				temp += c 
			if cut:
				sortedData.append(temp)
				temp = ""
			print(sortedData)
		if sortedData[0] == "560":
			self.connected = True

	def loginUser(self, username, password):
		self.sendData("560", username, password)

	def registerUser(self, username, password, email):
		self.sendData("561", username, password, email)

	def sendMessage(self, senderName, receiverName, content):
		self.sendData("562", senderName, receiverName, content)

	def disconnect(self):
		self.tcpsocket.close()

	