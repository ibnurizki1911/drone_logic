import numpy as np


def rx(roll):
     c = np.cos(roll)
     s = np.sin(roll)
     return np.array(
           [[1,0,0,0],
           [0,c,-s,0],
           [0,s,c,0],
           [0,0,0,1]]
     )

def ry(pitch):
     c = np.cos(pitch)
     s = np.sin(pitch)
     return np.array(
           [[c,0,s,0],
           [0,1,0,0],
           [-s,0,c,0],
           [0,0,0,1]]
     )
def rz(yaw):
     c = np.cos(yaw)
     s = np.sin(yaw)
     return np.array(
           [[c,-s,0,0],
           [s,c,0,0],
           [0,0,1,0],
           [0,0,0,1]]
     )

def eulerToMatrix(roll,pitch,yaw):
     return rz(yaw)@ry(pitch)@rx(roll)