#!/usr/bin/env python
# coding: utf-8
from kivy.app import App
from kivy.uix.button import Button
from client.client import *
from server.server import * 


server = Server('server/serverConfig.ini','DEFAULT')
server.start()
#start client Thread 
client = Client(5000)
client.start()

client.loginUser("igor","mdp")
client.sendMessage("thomas","igor","content")


class ClientApp(App):
    def build(self):
        return Button(text='Hello World')

ClientApp().run()