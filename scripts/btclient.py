# Client


import bluetooth
from time import sleep
import rospy


def main():
    

    rospy.init_node('btclient')

    bdAddr = rospy.get_param('~btaddr')

    print ('bt addr set to: ', bdAddr)

    port = 1

    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect ((bdAddr, port))

    while (1):
        for i in range(1,5):
            sock.send ("Hello Blue World!! " + str(i))

            sleep(1)
        
        sleep(4)

    sock.close()

    return


if __name__ == '__main__':
    main()