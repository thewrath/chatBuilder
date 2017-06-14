#!/usr/bin/env python
# coding: utf-8

import socket
import threading

from server.database import *

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
        self.COMMAND_LIST = ["560","561","562","563","565guygu"]
        self.username = ""
        self.password = ""
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
        self.sortData(receiveData.decode())

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
        
        self.clientsocket.send(dataToSend.encode())
       

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

        compt = 0
        while compt < len(sortedData):
            commandFind = False
            for command in self.COMMAND_LIST:
                if sortedData[compt] == command:
                    commandFind = True
                    print(sortedData[compt])
                    break
            if commandFind == True:
                if sortedData[compt] == "560" and not self.userConnected:
                    if self.database.loginUser(sortedData[compt+1], sortedData[compt+2]):
                        self.username = sortedData[compt+1]
                        self.password = sortedData[compt+2]
                        self.userConnected = True
                        self.sendData("560")
                    else:
                        self.sendData("065")
                    compt + 2
                elif sortedData[compt] == "565" and self.userConnected:
                    if self.username == sortedData[compt+1] and self.password == sortedData[compt+2]:
                        self.userConnected = False
                        self.sendData("565")
                elif sortedData[compt] == "561" and not self.userConnected:
                    if self.database.registerUser(sortedData[compt+1], sortedData[compt+2], sortedData[compt+3]):
                        self.userConnected = True
                        self.sendData("561")
                    else:
                        self.sendData("165")
                    compt = compt + 3
                elif sortedData[compt] == "563":
                    print("deconnexion")
                    self.clientConnected = False 
            compt = compt + 1 




        



