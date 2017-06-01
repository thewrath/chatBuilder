#!/usr/bin/env python
# coding: utf-8

import socket
import threading

"""
    ClientThread module
    ======================
"""

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
    	
    	"""
        Constructor of ClientThread.
 
        This initialise a new client thread with an ip
        a port and a socket
 
        :param ip: Client's IP
        :param port: Server port
        :rtype: void
    	"""

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 

    	"""
        Run method.
 
        Like another thread run method
       
        :rtype: void
    	"""
   
        print("Connection de %s %s" % (self.ip, self.port, ))

        print("Client déconnecté...")
