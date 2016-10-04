# importing modules
import threading
from socket import *
import time
import os
import random
from datetime import datetime
from urllib.request import urlopen

x_code = '###WAD#*#'


def getadr(): # get operating systems ipv4 address : used as server IP address
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("gmail.com",80))
    r = s.getsockname()[0]
    s.close()
    print('Server IP address : ', r)
    return (r)


def login():
    print('login waiting')
    while(1):
        port = 12001
        server_adr = getadr()
        serverSocket = socket(AF_INET,SOCK_STREAM) # make socket object
        serverSocket.bind((server_adr, port))
        serverSocket.listen(1)
        connectionSocket, addr = serverSocket.accept() # accepted connection
        in_1 = connectionSocket.recv(1024) # recieve from app
        print(in_1.decode())
    send1 = 'login'
    connectionSocket.send(send1.encode())
    print('login complete')

        

def moniter():
    print('moniter mode start')
    s1 = '8'
    s2 = '9'
    port = 12003
    server_adr = getadr()
    serverSocket = socket(AF_INET,SOCK_STREAM) # make socket object
    serverSocket.bind((server_adr, port))
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept() # accepted connection
    for i in range(10):
        connectionSocket.send(s1.encode())
        time.sleep(2)
        connectionSocket.send(s2.encode())
        time.sleep(1)
    print('moniter mode end')
        


def flight_ass():
    port = 12002
    server_adr = getadr()
    serverSocket = socket(AF_INET,SOCK_STREAM) # make socket object
    serverSocket.bind((server_adr, port))
    serverSocket.listen(1)
    print("flight ass mode start")
    connectionSocket, addr = serverSocket.accept() # accepted connection
    cKP = '2'
    cKK = '3'
    mKP = '2'
    mKK = '3'
    cubic = '[1,2,0]'
    canfly = '1'
    complexity = '0.02'
    asr = cKP + cKK + mKP + mKK + cubic + canfly + complexity
    connectionSocket.send(asr.encode())
    print("flight ass mode end")



while(1):
    stst = input("Login : L         Moniter : M          Fasst : F       $ ")
    if stst == 'l':
        login()
    elif stst =='m':
        moniter()
    elif stst =='f':
        flight_ass()
    else:
        continue
