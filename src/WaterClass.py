import numpy as np
import matplotlib.pyplot as plt

class Water:
    def __init__(self, position, velocity, charge, mass):
        '''
        This initialiser allows to create a water droplet. A water droplet is considered to be spherical.

        Paramaters
        ----------
        position: list
            Initial position of the drop in the format [x,y]
        velocity: list
            Initial velocity of the drop in the format [x,y]
        charge: float
            Charge in arbitrary unit
        mass: float
            Mass of the drop in arbitrary unit
        '''
        self.__x = [position[0]]
        self.__y = [position[1]]
        self.__velocity, self.charge, self.mass = np.array(velocity, dtype=float), charge, mass
        self.__speed = [self.get_speed()]

    def plotspeed(self):
        '''
        Allows to plot the speed of the drop as a function of time by plotting the log of all computed speeds.
        '''
        plt.title("Vitesse de la goutte d'eau en fonction du temps")
        plt.xlabel("Temps")
        plt.ylabel("Vitesse")
        plt.show()

    def update(self, dt, a):
        '''
        Allows to update the position and velocity of the water droplet. Takes the time interval and the velocity change as input.

        Paramaters
        ----------
        dt: float
            Time interval used for updating
        dv: np.array
            Acceleration on water drop
        '''

        dv = a * dt
        self.__velocity += dv
        self.__x.append(self.__x[-1] + self.__velocity[0]*dt)
        self.__y.append(self.__y[-1] + self.__velocity[1]*dt)
        self.__speed.append(self.get_speed())

    def get_speed(self):
        '''
        Returns the length of the current velocity vector
        '''
        return np.sqrt(np.sum(np.square(self.__velocity)))

    def get_position(self):
        '''
        Returns the current position of the water drop
        '''

        return np.array([self.__x[-1], self.__y[-1]])