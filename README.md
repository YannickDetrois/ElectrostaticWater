# Electrostatic Water

This project's aim is to simulate the trajectory of a water stream in a gravitational field and exposed to a charge. The stream is composed of water droplets (class Water) and is given a a radius, initial velocity and position, as well as a mass, charge and interaction potential parameters. The interaction between drops follows an attractive-repulsive potential similar to a Lennard-Jones potential. The charge (class Charge) has a fixed position and a charge. Both the charge and the droplet are considered to be points. Given a system (class System) with a specific gravitational constant and Coulomb constant, the position and velocity of the water droplet can be updated and plotted as a function of time. 

# Requirements

- Python >= 3.5
- numpy
- matplotlib

# Example of use

To see and test the experiment simulation, simply run file main.py on any IDE or in a terminal with the command:

```python3 main.py```

main.py contains a generic use of the classes, in which parameters can be manually changed to test different setups. For instance, a system with the following initial parameters

	####################################
	#### DEFINING SYSTEM PARAMETERS ####
	####################################
	
	gravity_constant = 9.81                #gravity constant on Earth's surface         [m/s^2]
	coulomb_constant = 8.988*pow(10,9)     #Coulomb constant                            [N⋅m^2⋅C^−2]
	miniumum_potential = 2*pow(10,-5)      #Lennard-Jones well depth U(r_min)           [J]
	minimum_radius = 0.001                 #Lennard-Jones minimum potential  is 2r_min  [m]
	simulation_time = 1                    #simulation time                             [s]
	time_step = 0.01                       #time step                                   [s]
	generation_time = 1                    #time in which new water spawns              [s]
	
	######### WATER PARAMETERS #########
	
	target_drop = 0                        #drop in the first row targetted for tracking
	water_velocity = np.array([0,-0.5])    #initial velocity of all water drops         [m/s]
	water_position = np.array([0.05,0.2])  #mean initial position of all water drops    [m]
	stream_radius = 0.01                   #radius of the water stream                  [m]
	charge_density = 5 * pow(10,-9)        #charge density of the water                 [C/m^2]
	mass_density = 1000                    #mass density of water                       [kg/m^2]
	
	######## CHARGE PARAMETERS #########
	
	charge_position = [0,0]                #position of the charge                      [m]
	charge = -0.1                          #value of the charge                         [C]

results in these outcomes for the trajectory animation:  

![velocity](/animations/animation.gif)

The velocity and acceleration curves of the water drop with index 0 are:

![trajectory](/figures/figure.png)
