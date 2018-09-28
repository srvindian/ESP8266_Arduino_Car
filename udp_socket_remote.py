# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:11:42 2018

@author: Sourav
"""

import socket
UDP_IP = '192.168.4.1'
UDP_PORT = 80
BUFFER_SIZE = 1024
#MESSAGE = b'%0'

if __name__ == "__main__":
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    s.connect((UDP_IP, UDP_PORT))
    # 0-stop,1-Left,2-Right,3-Forward,4-Backward
    while True:
        x = input('(0-4) : ')
        if x=='x':
            break
        MESSAGE = '%'+x+'\r\n'
        s.sendto(MESSAGE.encode(),(UDP_IP, UDP_PORT))
#    data = s.recv(BUFFER_SIZE)
    # -*- coding: utf-8 -*-



#For arduino<esp8266>
#  sendData("AT+RST\r\n",2000,DEBUG); // reset module
#  sendData("AT+CWMODE=3\r\n",1000,DEBUG); // configure as access point
#  sendData("AT+CIPMUX=1\r\n",1000,DEBUG); // configure for multiple connections
#  sendData("AT+CIPSTART=0,\"UDP\",\"192.168.4.1\",80,80,2\r\n",1000,DEBUG);
#  sendData("AT+CIPSEND=0,7,\"192.168.4.1\",80",1000,DEBUG); // turn on server on port 80