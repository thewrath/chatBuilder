#!/usr/bin/env python
# coding: utf-8
from kivy.app import App
#kivy.require("1.9.0")
from kivy.uix.button import Button
from client.client import *
from server.server import * 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

server = Server('server/serverConfig.ini','DEFAULT')
server.start()
#start client Thread 
client = Client(5000)
client.start()

class LoginScreen(Screen):
	def doLogin(self, username, password):
		
		client.loginUser(username, password)
		
		if client.userConnected:
			self.manager.current = "Main"

class MainScreen(Screen):
	def doLogout(self):
		client.disconnectUser()
		self.manager.current = "Login"
	def doSendMessage(self, message):
		print(message)

class ScreenManagement(ScreenManager):
	pass

appKv = Builder.load_file("my.kv")

class ClientApp(App):
	def build(self):
		return appKv

if __name__ == '__main__':
		
	ClientApp().run()
