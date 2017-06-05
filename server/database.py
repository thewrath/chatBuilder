#!/usr/bin/python2.7
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
		cur = self.conn.cursor()

		cur.execute("""
			CREATE TABLE IF NOT EXISTS users (id int(5) NOT NULL AUTO_INCREMENT, username varchar(50) DEFAULT NULL, 
			password varchar(50) DEFAULT NULL, email varchar(100) DEFAULT NULL, PRIMARY KEY(id) );
			""")
	
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
		    self.dispose()
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
			self.dispose()
			return register

	def dispose(self):
		self.conn.close()

