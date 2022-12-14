from SystemClass import *

####################################
#### DEFINING SYSTEM PARAMETERS ####
####################################

gravity_constant = 9.81                #gravity constant on Earth's surface         [m/s^2]
coulomb_constant = 8.988*pow(10,9)     #Coulomb constant                            [N⋅m^2⋅C^−2]
miniumum_potential = 1                 #Lennard-Jones well depth U(r_min)           [J]
minimum_radius = 1                  #Lennard-Jones minimum potential r_min       [m]
simulation_time = 5                    #simulation time                             [s]
time_step = 0.1                        #time step                                   [s]
generation_time = 0                    #time in which new water spawns              [s]

######### WATER PARAMETERS #########

water_velocity = np.array([2,2])       #initial velocity of all water drops         [m/s]
water_position = np.array([0,20])      #mean initial position of all water drops    [m]
stream_radius = 1                    #radius of the water stream                  [m]
charge_density = pow(10,-7)        #charge density of the water                 [C/m^3]
mass_density = 1                       #mass density of water                       [kg/m^3]

######## CHARGE PARAMETERS #########

charge_position = [0,0]                #position of the charge                      [m]
charge = -1                            #value of the charge                         [C]


s = System(gravity_constant, coulomb_constant, miniumum_potential, minimum_radius, simulation_time, time_step, generation_time,
             water_velocity, water_position, stream_radius, charge_density, mass_density, charge_position, charge)
s.animate(1, 'animation')