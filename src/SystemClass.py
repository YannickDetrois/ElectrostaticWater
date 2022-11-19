import numpy as np
import matplotlib.pyplot as plt

class System:
    def __init__(self, water, charge, gravity_constant, coulomb_constant):
        self.__water, self.__charge, self.__g, self.__k = water, charge, gravity_constant, coulomb_constant

    def plot(self):
        plt.title("Trajectoire de la goutte d'eau")
        plt.xlabel("x")
        plt.ylabel("y")
        self.__water.plot()
        self.__charge.plot()
        plt.legend()
        plt.show()

    def update(self, dt):
        r = np.array(self.__water.get_position())-np.array(self.__charge.get_position())
        r2 = np.sum(np.square(r))
        r = r/np.sqrt(r2)
        a = self.__k * self.__water.charge * self.__charge.charge / (r2 * self.__water.mass) * r - np.array([0,self.__g])
        dv = a * dt 
        self.__water.update(dt, dv)

    