import struct, os
import time
import math
import numpy as np
import matplotlib.pyplot as plt
opticaly=[]
opticalx=[]
 
file = open( "/dev/input/mice", "rb" );
 
point_x = 0
point_y = 0
 
class Point:
    x = 0.0
    y = 0.0
 
def getMouseEvent():
    buf = file.read(3); 
    x,y = struct.unpack( "bb", buf[1:] );
    dis = Point();
    dis.x = x;
    dis.y = y;
    return dis;  

def getxyv():
    global point_x ,v
    global point_y       
    dis = getMouseEvent()
    point_x = point_x + dis.x
    point_y = point_y + dis.y
    print ("%d  %d" % (point_x*0.027, point_y*0.027))

for i in range(50):
    getxyv()
    opticaly.append(point_y*0.027)
    opticalx.append(point_x*0.027)
    time.sleep(0.1)
plt.subplot(1, 1, 1)
plt.plot(opticaly, opticalx)
plt.title('OP-DATA')
plt.ylabel('Y')
plt.xlabel('X')
plt.show()
f.close()

