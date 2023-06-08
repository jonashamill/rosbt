#!/usr/bin/env python


# Server


import bluetooth
from time import sleep
import rospy


def main():

    serverSock = bluetooth.BluetoothSocket( bluetooth.RFCOMM)

    port = 1 
    serverSock.bind(("", port))
    serverSock.listen(1)

    clientSock, address = serverSock.accept()
    print ("Accepted connection from: ", address)

    while (1):
        data = clientSock.recv(1024)
        print ("recieved [%s]" % data)
    
    return




if __name__ == '__main__':
    main()