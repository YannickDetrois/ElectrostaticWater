import numpy as np
import matplotlib.pyplot as plt
from WaterClass import *
from ChargeClass import *
from SystemClass import *

w = Water([2,10], [0,1], -1, 0.5)
q = Charge([2.5,8], -1)
s = System(w, q, 5, 0.1)
for a in range(30): s.update(0.1)
s.plot()