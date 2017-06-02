#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import MySQLdb

class Database:

	def __init__(self, plocalhost, puser, ppassword, pdatabase):

		self.conn = MySQLdb.connect(host=plocalhost,user=puser,passwd=ppassword, db=pdatabase)
		self.cursor = self.conn.cursor()

		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS users (id int(5) NOT NULL AUTO_INCREMENT, username varchar(50) DEFAULT NULL, 
			password varchar(50) DEFAULT NULL, email varchar(100) DEFAULT NULL, PRIMARY KEY(id) );
			""")
	
	def loginUser(self, username, password):
		self.cursor.execute("""SELECT id FROM users WHERE username=? AND password=? """, (username,password,))
		rows = self.cursor.fetchall()
		for row in rows:
			return True
		return False

	def dispose(self):
		self.conn.close()


db = Database("localhost","root","root","chatAppDB")
print db.loginUser("pierre","mdp")
