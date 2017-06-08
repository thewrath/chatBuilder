#!/usr/bin/env python
# coding: utf-8

from client.client import *
from server.server import * 


server = Server('server/serverConfig.ini','DEFAULT')
server.start()
#start client Thread 
client = Client()
client.start()

client.loginUser("igor","mdp")
client.sendMessage("thomas","igor","content")

