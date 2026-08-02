import numpy as np

class Motor:
    def __init__(self,ax,position,color):
         self.position = position
         self.p = 0
         self.color = color

         self.point, = ax.plot(
              [],[],[],'o',color= color,markersize=8
         )
 
    def update(self,R):

        self.p = R @ self.position

        self.point.set_data([self.p[0]],[self.p[1]])
        self.point.set_3d_properties(self.p[2])


          
class Arm:
    def __init__(self,ax):
        self.line, = ax.plot([],[],[], "k", linewidth=3)

    def update(self,p1,p2):

        self.line.set_data(
            [p1[0], p2[0]],
            [p1[1], p2[1]]
        )

        self.line.set_3d_properties(
            [p1[2],p2[2]]
        )
