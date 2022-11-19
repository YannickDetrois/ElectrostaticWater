import numpy as np
import matplotlib.pyplot as plt

class Water:
    def __init__(self, position, velocity, charge, mass):
        self.__x = [position[0]]
        self.__y = [position[1]]
        self.__vx = velocity[0]
        self.__vy = velocity[1]
        self.charge, self.mass = charge, mass

    def plot(self):
        plt.plot(self.__x, self.__y, 'b')

    def update(self, dt, dv):
        self.__vx += dv[0]
        self.__vy += dv[1]
        self.__x.append(self.__x[-1] + self.__vx*dt)
        self.__y.append(self.__y[-1] + self.__vy*dt)

    def get_position(self):
        return [self.__x[-1], self.__y[-1]]

    