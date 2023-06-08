# Client


import bluetooth
from time import sleep

def main():
    
    bdAddr = '3C:21:9C:E0:88:54'

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