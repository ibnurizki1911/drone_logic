# import numpy as np
# import matplotlib.pyplot as plt

class Frame:

    def __init__(self,ax):
         self.frame = self.buildFrame(ax)

    def buildFrame(self,ax):

            x, = ax.plot([],[],[], color="r")
            y, = ax.plot([],[],[], color="g")
            z, = ax.plot([0,0],[0,0],[0,0], color="b")

            return x,y,z


    def update(self,T,scale = 30):
        x_line,y_line,z_line = self.frame

        R = T[:3,:3]

        P = T[:3, 3]

        x = R[:,0] * scale + P
        y = R[:,1] * scale + P
        z = R[:,2] * scale + P

        x_line.set_data([P[0],x[0]],[P[1],x[1]])
        x_line.set_3d_properties([P[2],x[2]])

        y_line.set_data([P[0],y[0]],[P[1],y[1]])
        y_line.set_3d_properties([P[2],y[2]])

        z_line.set_data([P[0],z[0]],[P[1],z[1]])
        z_line.set_3d_properties([P[2],z[2]])
