import numpy as np
import matplotlib.pyplot as plt

class Charge:
    
    def __init__(self, position, charge):
        '''
        This initialiser allows to create an immobile point charge.

        Paramaters
        ----------
        position: list
            Position of the charge in the format [x,y]
        charge: float
            Charge in arbitrary unit
        '''
        self.__x = position[0]
        self.__y = position[1]
        self.charge = charge

    def get_position(self):
        '''
        Returns a list with the position of the charge.
        '''
        return np.array([self.__x, self.__y])

    