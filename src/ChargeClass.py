import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

class Charge:
    def __init__(self, position, charge):
        self.__x = position[0]
        self.__y = position[1]
        self.charge = charge

    def plot(self):
        plt.plot(self.__x, self.__y, 'r+')

    def get_position(self):
        return [self.__x, self.__y]

    