# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:19:30 2018

@author: Sourav
"""
import cv2
import numpy as np
import socket
#%%
UDP_IP = '192.168.4.1'
UDP_PORT = 80
BUFFER_SIZE = 1024
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
move={-1:0,97:1,100:2,119:3,115:4,27:5}
orient={0:'Stop',1:'Left',2:'Right',3:'Forward',4:'Backward'}
while True:
    img=np.zeros((100,200,3),dtype=np.uint8)
    key=cv2.waitKey(200)
    #0-stop,1-Left,2-Right,3-Forward,4-Backward
    if key!=27:
        x=move[key]
        print(orient[x])
        MESSAGE = '%'+str(x)+'\r\n'
#        print(MESSAGE)
        s.sendto(MESSAGE.encode(),(UDP_IP, UDP_PORT))
        cv2.putText(img,orient[x], (50,50), cv2.FONT_HERSHEY_SIMPLEX,1, (0,255,0), 4)
        cv2.imshow("Remote",img)
    else:
        break
cv2.destroyAllWindows()
    
