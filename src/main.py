from WaterClass import *
from ChargeClass import *
from SystemClass import *

w = Water([2,100], [.03,0.], -10, 1)
q = Charge([0,0], -50)
s = System(w, q, 0.5, 1)
for a in range(7000): s.update(0.01)
s.plot()
w.plotspeed()