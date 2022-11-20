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

    def plot(self):
        '''
        Allows to plot the charge as a red plus sign.
        '''
        plt.plot(self.__x, self.__y, 'r+', label='charge = {}'.format(self.charge))

    def get_position(self):
        '''
        Returns a list with the position of the charge.
        '''
        return [self.__x, self.__y]

    