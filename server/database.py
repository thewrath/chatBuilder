#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import mysql.connector

class Database:

	def __init__(self, plocalhost, puser, ppassword, pdatabase):

		self.conn = mysql.connector.connect(host=plocalhost,user=puser,password=ppassword, database=pdatabase)
		self.cursor = self.conn.cursor()

		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS users (id int(5) NOT NULL AUTO_INCREMENT, username varchar(50) DEFAULT NULL, 
			password varchar(50) DEFAULT NULL, email varchar(100) DEFAULT NULL, PRIMARY KEY(id) );
			""")
	
	def loginUser(self, username, password):


	def registerUser(self, username, password, email):

	def storeMsg(self, sender, receiver, content):

	def findLastMsg(self, sender, receiver):

	def dispose(self):
		self.conn.close()

