class PController:

    def __init__(self,kp,ki,kd,i_limit):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.integral = 0
        self.i_limit = i_limit 

        self.previous_error = 0

    def update(self, target,actual,dt):

        eror = target - actual

        self.integral += eror *dt

        if self.integral > self.i_limit:
            self.integral = self.i_limit

        if self.integral < -self.i_limit:
            self.integral = -self.i_limit

        # Derivative
        derivative = (eror - self.previous_error) / dt

        # buffer error untuk loop berikutnya
        self.previous_error = eror
            
        output = (self.kp * eror
                + self.ki * self.integral
                + self.kd * derivative
                )
        return output