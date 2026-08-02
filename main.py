import numpy as np
import matplotlib.pyplot as plt
import mpu
from frame import Frame
from drone.body import Drone
import math3d as md

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
ax.set_zlim(0,200)


# ====== Setup ======
#  FRAME 
ori = Frame(ax)
frame1 = Frame(ax)

# BODY
drone = Drone(ax,50)
O = np.eye(4)
ori.update(O,scale=50)


# ======= LOOPING ========
while plt.fignum_exists(fig.number):


      _,r,p,y  = mpu.parsData()

      try:
          roll = np.radians(float(r))
          pitch = np.radians(float(p))
          yaw = np.radians(float(y))
      except ValueError:
           print("sinyal tidajk diketahui")
           continue

      T = md.eulerToMatrix(roll,pitch,yaw)
      frame1.update(T)
      drone.update(T)


      plt.pause(0.01)
