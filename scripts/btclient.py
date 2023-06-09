#!/usr/bin/env python3


# Client


import bluetooth
from time import sleep
import rospy


def main():
    

    rospy.init_node('btclient')

    # try:
    bdAddr = rospy.get_param('btaddr')
    mssg = rospy.get_param('mssg')
    
    # except: 
    #     bdAddr = '3C:21:9C:E0:88:54'

    print ('bt addr set to: ', bdAddr)

    port = 1

    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect ((bdAddr, port))

    while (1):
        for i in range(1,5):
            sock.send (mssg + str(i))

            sleep(1)
        
        sleep(4)

    sock.close()

    return


if __name__ == '__main__':
    main()