#!/usr/bin/env python
# coding: utf-8

import socket
import threading

from database import *

"""
    ClientThread module
    ======================
"""

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket, db):
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
        self.bufLen = 2048
        self.userConnected = False
        self.clientConnected = True
        self.database = db
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port))

    def run(self):
        """
        Run method.
 
        Like another thread run method
       
        :rtype: void
        """
   
        print("Connection de %s %s" % (self.ip, self.port))
        while(self.clientConnected):
            self.receiveData()
        print("Client déconnecté...")

    def receiveData(self):

        """

        ReceiveData method.

        Used to receive data send by the client.
        :rtype: void

        """

        receiveData = self.clientsocket.recv(self.bufLen)

        self.sortData(receiveData)

    def sendData(self, *datas):
        dataToSend = "&"
        count = len(datas)
        for data in datas:
            count = count - 1
            dataToSend += data
            if not count == 1:
                dataToSend += "&&"
            else:
                dataToSend += "&"
                print(dataToSend)

    def sortData(self, data):

        """

        SortData method.

        Used to sort data receive from the socket.

        :param data: data receive from the socket 
        :rtype: void

        """
        sortedData = []
        temp = ""
        cut = True
        for c in data:
            if c == '&':
                if cut:
                    cut = False
                else:
                    cut = True
            else:
                temp += c 
            if cut:
                sortedData.append(temp)
                temp = ""       
        print(sortedData)

        if len(sortedData) >= 3:
            if(sortedData[0] == "560" and not self.userConnected):
                if self.database.loginUser(sortedData[1], sortedData[2]):
                    self.userConnected = True
                    self.sendData("560")
                else:
                    self.sendData("065")

            elif(sortedData[0] == "561" and not self.userConnected):
                if self.database.registerUser(sortedData[1], sortedData[2], sortedData[3]):
                    self.userConnected = True
                    self.sendData("561")
                else:
                    self.sendData("165") 



