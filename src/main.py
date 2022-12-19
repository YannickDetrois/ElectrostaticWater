from SystemClass import *

####################################
#### DEFINING SYSTEM PARAMETERS ####
####################################

gravity_constant = 9.81                #gravity constant on Earth's surface         [m/s^2]
coulomb_constant = 8.988*pow(10,9)     #Coulomb constant                            [N⋅m^2⋅C^−2]
miniumum_potential = 0.05              #Lennard-Jones well depth U(r_min)           [J]
minimum_radius = 0.1                   #Lennard-Jones minimum potential  is 2r_min  [cm]
simulation_time = 3                    #simulation time                             [s]
time_step = 0.1                        #time step                                   [s]
generation_time = 2                    #time in which new water spawns              [s]

######### WATER PARAMETERS #########

target_drop = 0                        #drop in the first row targetted for tracking
water_velocity = np.array([0,-5])      #initial velocity of all water drops         [m/s]
water_position = np.array([5,20])      #mean initial position of all water drops    [cm]
stream_radius = 1                      #radius of the water stream                  [cm]
charge_density = 5 * pow(10,-9)        #charge density of the water                 [C/m^2]
mass_density = 1                       #mass density of water                       [kg/m^2]

######## CHARGE PARAMETERS #########

charge_position = [0,0]                #position of the charge                      [m]
charge = -1                            #value of the charge                         [C]


s = System(gravity_constant, coulomb_constant, miniumum_potential, minimum_radius, simulation_time, time_step, generation_time, target_drop,
             water_velocity, water_position, stream_radius, charge_density, mass_density, charge_position, charge)
s.animate(1, 1, "animation1", "figure1")
#s.animate()