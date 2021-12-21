from re import A
import tensorflow as tf
import math

class DiffEq():
    """
    This class defines the different differential
    equations used.
    """

    def __init__(self, diffeq, x, y, dydx, d2ydx2, a, b):
        """
        diffeq : name of the differential equation used (ex: diffeq = "first order ode")
        """

        self.diffeq = diffeq
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.dydx = dydx
        self.d2ydx2 = d2ydx2
        #hbar = 1, m = 1, omega = 1
        #Customize the energy level with n
        if self.diffeq == "experiment_1":
            self.eq = (self.a + self.b) * self.d2ydx2 - self.dydx - self.y

        if self.diffeq == "experiment_2":
            self.eq = -(self.a - (self.b * (math.e ** -self.x))) * self.d2ydx2 - (math.e ** -self.x)*self.dydx - (self.x * self.y)

