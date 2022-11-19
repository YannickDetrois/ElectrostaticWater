import numpy as np
import matplotlib.pyplot as plt

class Water:
    def __init__(self, position, velocity, charge, mass):
        self.__x = [position[0]]
        self.__y = [position[1]]
        self.__velocity, self.charge, self.mass = np.array(velocity), charge, mass
        self.__speed = [self.get_speed()]
        self.__time = [0]

    def plot(self):
        plt.plot(self.__x, self.__y, 'b', label="goutte d'eau: charge = {}, masse = {}".format(self.charge, self.mass))

    def plotspeed(self):
        plt.title("Vitesse de la goutte d'eau en fonction du temps")
        plt.xlabel("Temps")
        plt.ylabel("Vitesse")
        plt.plot(self.__time, self.__speed)
        plt.show()

    def update(self, dt, dv):
        self.__velocity += dv
        self.__x.append(self.__x[-1] + self.__velocity[0]*dt)
        self.__y.append(self.__y[-1] + self.__velocity[1]*dt)
        self.__speed.append(self.get_speed())
        self.__time.append(self.__time[-1]+dt)

    def get_speed(self):
        return np.sqrt(np.sum(np.square(self.__velocity)))

    def get_position(self):
        return [self.__x[-1], self.__y[-1]]

    