#!/usr/bin/env python
# coding: utf-8

from client import *

client = Client(5000)

#start client Thread 
client.start()

client.loginUser("igor","mdp")
client.sendMessage("thomas","igor","content")

