import numpy as np
from .kit import Motor,Arm


class Drone:
    def __init__(self,ax,L = 30):

        self.arm1 = Arm(ax)
        self.arm2 = Arm(ax)

        self.m1 = Motor(ax, np.array([ L, L, 0]),"b")
        self.m2 = Motor(ax, np.array([ L,-L, 0]),"r")
        self.m3 = Motor(ax, np.array([-L,-L, 0]),"g")
        self.m4 = Motor(ax, np.array([-L, L, 0]),"y")

    def update(self,T):

        R = T[:3,:3]

        self.m1.update(R)
        self.m2.update(R)
        self.m3.update(R)
        self.m4.update(R)

        self.arm1.update(
            self.m1.p,
            self.m3.p

        )

        self.arm2.update(
            self.m2.p,
            self.m4.p
        )

