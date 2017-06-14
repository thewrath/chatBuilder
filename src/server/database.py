#!/usr/bin/python3
#-*- coding: utf-8 -*-

import pymysql

class Database:

	def __init__(self, host, user, passwd, db):

		self.conn = pymysql.connect(host=host,
                             user=user,
                             password=passwd,
                             db=db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
		cursor = self.conn.cursor()

		cursor.execute("""
			CREATE TABLE IF NOT EXISTS users (id int(5) NOT NULL AUTO_INCREMENT, username varchar(50) DEFAULT NULL, 
			password varchar(50) DEFAULT NULL, email varchar(100) DEFAULT NULL, PRIMARY KEY(id) );
			""")
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS messages (id int(5) NOT NULL AUTO_INCREMENT, sender varchar(50) DEFAULT NULL, 
			receiver varchar(50) DEFAULT NULL, content varchar(1000) DEFAULT NULL, PRIMARY KEY(id) );
			""")
		cursor.close()

	
	def loginUser(self, username, password):
		find = False
		try:
		    with self.conn.cursor() as cursor:
		        # Read a single record
		        sql = "SELECT `id` FROM `users` WHERE `username`=%s AND `password` =%s"
		        cursor.execute(sql, (username,password))
		        result = cursor.fetchone()
		        if result:
		        	find = True
		finally:
		    return find

	def registerUser(self, username, password, email):
		register = False
		try:
			with self.conn.cursor() as cursor:
				sql = "SELECT `id` FROM `users` WHERE `username`=%s OR `email`=%s "
				cursor.execute(sql, (username,email))
				result = cursor.fetchone()	
				if result:
					register = False
				else:
					sql = "INSERT INTO `users` (`username`, `password`,`email`) VALUES (%s, %s, %s)"
					cursor.execute(sql, (username, password, email))
					self.conn.commit()
					register = True
		finally:
			return register

	def test(args, types):
		for a, t in zip(args, types):
			if not isinstance(a, t):
				return False
			else:
				return True

	def saveMsg(self, sender, receiver, content):	
		saved = False	
		if not test((sender, receiver, content), (str, str, str)):
			raise TypeError("Mauvais type")
		try:
			with self.conn.cursor() as cursor:				
				sql = "INSERT INTO `message` (`sender`, `receiver`, `content`) VALUES (%s, %s, %s)"
				cursor.execute(sql, (sender, receiver, content))
				self.conn.commit()
				saved = True
		finally:
			return saved

	def findMsg(self, sender, receiver):
		find = False
		try:
			with self.conn.cursor() as cursor:
				sql = "SELECT `content` FROM `message` WHERE `sender`=%s AND `receiver`=%s ORDER BY `id` DESC LIMIT 1"
				cursor.execute(sql, (sender, receiver))
				result = cursor.fetchone()
				if result:
					find = True
				else:
					print("No available messages")
					find = False
		finally:
			return find

	def dispose(self):
		self.conn.close()

