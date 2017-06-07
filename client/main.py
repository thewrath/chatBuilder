#!/usr/bin/env python
# coding: utf-8

from client import *

client = Client()

#start client Thread 
client.start()

client.loginUser("igor","mdp")
