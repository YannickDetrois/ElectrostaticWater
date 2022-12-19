from SystemClass import *

####################################
#### DEFINING SYSTEM PARAMETERS ####
####################################

gravity_constant = 9.81                #gravity constant on Earth's surface         [m/s^2]
coulomb_constant = 8.988*pow(10,9)     #Coulomb constant                            [N⋅m^2⋅C^−2]
miniumum_potential = 2*pow(10,-8)      #Lennard-Jones well depth U(r_min)           [J]
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
mass_density = 1                       #mass density of water                       [kg/m^2]

######## CHARGE PARAMETERS #########

charge_position = [0,0]                #position of the charge                      [m]
charge = -0.0001                       #value of the charge                         [C]


s = System(gravity_constant, coulomb_constant, miniumum_potential, minimum_radius, simulation_time, time_step, generation_time, target_drop,
             water_velocity, water_position, stream_radius, charge_density, mass_density, charge_position, charge)
#s.animate(0, 1, "animation22")
s.animate()