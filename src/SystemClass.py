import numpy as np
import matplotlib.pyplot as plt

class System:
    def __init__(self, water, charge, gravity_constant, coulomb_constant):
        '''
        This initialiser allows to create a system, which is composed of environmental parameters defining the water drop experiment.

        Paramaters
        ----------
        water: Water
            Drop of water used for the experiment
        charge: Charge
            Charge used in the experiment
        gravity_constant: float
            Gravity constant use for the gravitational force computations in arbitrary unit
        coulomb_constant: float
            Constant used like the Coulomb constant term in the Coulomb force expression
        '''
        self.__water, self.__charge, self.__g, self.__k = water, charge, gravity_constant, coulomb_constant

    def plot(self):
        '''
        Allows to plot the trajectory of the drop and the charge in one figure.
        '''
        plt.title("Trajectoire de la goutte d'eau")
        plt.xlabel("x")
        plt.ylabel("y")
        self.__water.plot()
        self.__charge.plot()
        plt.legend()
        plt.show()

    def update(self, dt):
        '''
        Computes and operates the velocity vector change of the water drop in the environment given electrical and gravitational parameters.

        Paramaters
        ----------
        dt: float
            Time interval used for updating
        '''

        # Components of acceleration are determined by Newton's law for both gravitational and electromagnetic forces
        r = np.array(self.__water.get_position())-np.array(self.__charge.get_position())
        r2 = np.sum(np.square(r))
        r = r/np.sqrt(r2)
        a = self.__k * self.__water.charge * self.__charge.charge / (r2 * self.__water.mass) * r - np.array([0,self.__g])
        
        # Using that a = dv/dt to find an expression for the change in velocity
        dv = a * dt 
        self.__water.update(dt, dv)

    