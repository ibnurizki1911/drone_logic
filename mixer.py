class Mixer:
    def __init__(self):
        self.m1 = 0
        self.m2 = 0
        self.m3 = 0
        self.m4 = 0

    def update(self, thorttle,roll,pitch,yaw):
        self.m1 = thorttle + roll - pitch
        self.m2 = thorttle - roll - pitch
        self.m3 = thorttle - roll + pitch
        self.m4 = thorttle + roll + pitch

        return self.m1,self.m2,self.m3,self.m4


mixer = Mixer()

motor_rpm = mixer.update(thorttle=1000,roll=0,pitch=100,yaw=0)
print(motor_rpm)
