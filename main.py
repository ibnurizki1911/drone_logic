import numpy as np
import time
import matplotlib.pyplot as plt
import mpu as mpu
from frame import Frame
from drone.body import Drone
import math3d as md
from mixer import Mixer
from pid import PController as pctr

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
ax.set_zlim(0,200)

roll =0
pitch =0
yaw =0

def on_key(event):
    speed = np.radians(5)
    global roll,pitch,yaw
    if event.key == 'w':
        roll += speed
    if event.key == 'e':
        roll -= speed
    if event.key == 'd':
        pitch += speed
    if event.key == 'a':
        pitch -= speed
    if event.key == 'x':
        yaw += speed
    if event.key == 'z':
        yaw -= speed
        

fig.canvas.mpl_connect(
    'key_press_event',
    on_key
)


# ====== Setup ======
#  FRAME 
ori = Frame(ax)
frame1 = Frame(ax)

# BODY
drone = Drone(ax,50)
O = np.eye(4)
ori.update(O,scale=50)
mix = Mixer()
roll_pid = pctr(20,0.1,10)
pitch_pid = pctr(20.0,0.1,10)
yaw_pid = pctr(20,0.1,10)
d_ferst = time.perf_counter()



# ======= LOOPING ========
while plt.fignum_exists(fig.number):


      _,r,p,y  = mpu.parsData()

      try:
          roll_raw = np.radians(float(r))
          pitch_raw = np.radians(float(p))
          yaw_raw = np.radians(float(y))
      except ValueError:
           print("sinyal tidajk diketahui")
           continue
      d_now = time.perf_counter()
      dt = d_now - d_ferst
      d_ferst = d_now
      roll_out = roll_pid.update(target=roll,actual=roll_raw,dt=dt)
      pitch_out = pitch_pid.update(target=pitch,actual=pitch_raw,dt=dt)
      yaw_out = yaw_pid.update(target=yaw,actual=yaw_raw,dt=dt)

      m1,m2,m3,m4 = mix.update(
           thorttle=1000,
           roll=roll_out,
           pitch=pitch_out,
           yaw=yaw_raw
      )

    #   print(roll,pitch,yaw)
      
      print("biru:",m1)
      print('merah:',m2)
      print("hijau",m3)
      print("kuning",m4)

      target = md.eulerToMatrix(roll,pitch,yaw)  
    #   T = md.eulerToMatrix(roll_out,pitch_out,yaw_out)
      T = md.eulerToMatrix(
          roll_raw,pitch_raw,yaw_raw)
      frame1.update(target)

      drone.update(T)
      drone.m1.setRPM(m1)
      drone.m2.setRPM(m2)
      drone.m3.setRPM(m3)
      drone.m4.setRPM(m4)
    


      plt.pause(0.01)
