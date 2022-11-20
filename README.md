# Electrostatic Water

This project's aim is to simulate the trajectory of a water droplet in a gravitational field and exposed to a charge. The water droplet (class Water) is given an initial velocity and position, as well as a mass and charge. The charge (class Charge) has a fixed position and a charge. Both the charge and the droplet are considered to be points. Given a system (class System) with a specific gravitational constant and Coulomb constant, the position and velocity of the water droplet can be updated and plotted as a function of time. 

# Requirements

- Python >= 3.5
- numpy
- matplotlib

# Example of use

To see and test the experiment simulation, simply run file main.py on any IDE or in a terminal with the command:

```python3 main.py```

main.py contains a generic use of the classes, in which parameters can be manually changed to test different setups. For instance, a water drop with initial position (2,100), initial velocity (0.,0.), charge -10 and mass 1, a charge with position (0,0) and charge -50 and a system with gravitational constant 0.5 and Coulomb constant 1 gives:

![trajectory](/images/spee1.png)
![velocity](/images/traj1.png)