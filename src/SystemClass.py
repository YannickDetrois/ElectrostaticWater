import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.animation as animation
import os
from WaterClass import *
from ChargeClass import *

class System:
   def __init__(self, gravity_constant, coulomb_constant, minimum_potential, minimum_radius, simulation_time, time_step, generation_time,
            target_drop, water_velocity, water_position, stream_radius, charge_density, mass_density, charge_position, charge):
      '''
      This initialiser allows to create a system, which is composed of environmental parameters defining the water drop experiment.

      Paramaters
      ----------
      gravity_constant: float
         gravity constant on Earth's surface        [m/s^2]
      coulomb_constant: float
         Coulomb constant                            [N⋅m^2⋅C^-2]
      minimum_potential: float
         Lennard-Jones well depth U(r_min)           [J]
      miniumum_radius: float                 
         Lennard-Jones r_min                         [m]
      simulation_time: float                
         simulation time                             [s]
      time_step: float             
         time step                                   [s]
      generation_time: float                
         time in which new water spawns              [s]


      water_velocity: 2D np.array             
         initial velocity of all water drops         [m/s]
      water_position: 2D np.array           
         mean initial position of all water drops    [m]
      stream_radius: float              
         radius of the water stream                  [m]
      charge_density: float                 
         charge density of the water                 [C/m^2]
      mass_density: float                 
         mass density of the water                   [kg/m^2]


      charge_position: 2D np.array             
         position of the charge                      [m]
      charge: float
         value of the charge                         [C]
      '''

      self._gravity_constant = gravity_constant
      self._coulomb_constant = coulomb_constant 
      self._epsilon_LJ = minimum_potential
      self._simulation_time = simulation_time 
      self._time_step = time_step 
      self._generation_time = generation_time
      self._time = np.arange(0,simulation_time,time_step)     #starting time at 0, up to t and with steps dt
      self._water_position = water_position
      self._water_velocity = water_velocity
      
      ### INITIALISING WATER DROPS ###
      self._init_water(minimum_radius, stream_radius, charge_density, mass_density, target_drop)

      ### INITIALISING CHARGE ###
      self._charge = Charge(charge_position, charge)

      ### INITIALISING PLOT PARAMETERS ###
      self._init_figure_parameters()
      self.update_plot()

   def _init_water(self, minimum_radius, stream_radius, charge_density, mass_density, target_drop):
      
      #Determine how many water drops fit in the stream
      
      self._drop_diameter = 2 * minimum_radius                           #diameter of a water droplet
      self._sigma_LJ = self._drop_diameter / 2                 #diameter of one water droplet = d_min = 2^(1/6)*s (real valued positive solution)
      self._number_drops = int((2*stream_radius) // self._drop_diameter) #integer number of water drops that fit in the stream diameter (x direction)
      self._stream_radius = self._number_drops * self._drop_diameter / 2 #radius of the largest possible water stream with given dmin

      if self._number_drops == 0: raise ValueError("The radius of one water drop is bigger than the stream radius entered")
      #print("water_diameter", self._drop_diameter, "number of drops", self._number_drops, "stream radius", self._stream_radius, "sigma radius", self._sigma_radius)

      if target_drop >= self._number_drops: raise ValueError("You can only track velocity and acceleration of a drop with index in [0, number_drops[")
      self._target_drop = target_drop

      #water stream is generated along a line perpendicular to the velocity
      if np.all(self._water_velocity==0):
         self._v_orth = np.array([1, 0])
      else:
         self._v_orth = np.array([self._water_velocity[1], -self._water_velocity[0]])  
         self._v_orth = self._v_orth/np.linalg.norm(self._v_orth)

      # vector along which new water molecules are spawed
      self._water_spawn_position = np.empty((self._number_drops, 2))
      for n in range(self._number_drops):
         self._water_spawn_position[n] = self._water_position + (self._stream_radius - self._drop_diameter / 2 - n * self._drop_diameter) * self._v_orth

      water_volume = np.pi * pow(self._drop_diameter/2, 2)            #in 2D, so assuming water drops are circular and not spherical
      self._water_charge = water_volume * charge_density              #charge of a water droplet
      self._water_mass = water_volume * mass_density                  #mass of a water droplet
      print("Mass of a water drop: {}kg".format(self._water_mass))
      print("Charge of a water drop: {}C".format(self._water_charge))

      self._water = []
      self.new_water()

   def _init_figure_parameters(self):
      '''
      Allows to initialise the plot, setting title, dimensions, ...
      '''
      xlimleft = -0.01
      xlimright = 0.1
      ylimlow = -0.5
      ylimhigh = 0.2
      self._deltaxlim = xlimright - xlimleft

      width = 6
      height = 6
      self._dots_per_inch = 100
      dots_in_width = width * self._dots_per_inch
      self._dots_per_x = dots_in_width / self._deltaxlim * 1.1

      
      self._figure = figure(figsize=(width, height), dpi=self._dots_per_inch)
      axis = plt.axes(xlim=(xlimleft,xlimright),  ylim=(ylimlow,ylimhigh))
      axis.set_title("Trajectoire du filet d'eau")
      axis.set_xlabel(r'x [m]')
      axis.set_ylabel(r'y [m]')
      
      # initializing a line variable
      self._line_water, self._line_charge, = axis.plot([], [], [], [], lw=0)

   def new_water(self):
      
         for p in self._water_spawn_position:
            self._water.append(Water(p, self._water_velocity, self._water_charge, self._water_mass))

   def update_plot(self):
      '''
      Allows to plot the trajectory of the drop and the charge in one figure.
      '''
      
      water_positions = np.array([water.get_position() for water in self._water])
      charge_position = self._charge.get_position()

      #Plotting water drops
      self._line_water.set_data(water_positions[:,0], water_positions[:,1])
      self._line_water.set_color('b')
      self._line_water.set_marker('o')
      self._line_water.set_markersize(self._drop_diameter * self._dots_per_x / 2)
      #, label="goutte d'eau: charge = {}, masse = {}".format(self.charge, self.mass)
      #plt.fill_between(water_positions[:,0], water_positions[:,1])

      # Plotting charge
      self._line_charge.set_data(charge_position[0], charge_position[1])
      self._line_charge.set_color('r')
      self._line_charge.set_marker('+')
      self._line_charge.set_markersize(self._dots_per_x * self._deltaxlim / 40)
      #, label='charge = {}'.format(self.charge)

      return self._line_water, self._line_charge,

   def update(self, frame):
      '''
      Computes and operates the velocity vector change of the water drop in the environment given electrical and gravitational parameters.
      Additionally, computes velocity change due to a Lennard-Jones potential between adjacent water drops.

      Paramaters
      ----------
      dt: float
         Time interval used for updating
      '''
      # Components of acceleration are determined by Newton's law for both gravitational and electromagnetic forces and a Lennard-Jones potential
   
      # Gravitational force
      a_grav = - np.array([0,self._gravity_constant])
      a_lejo = np.zeros((len(self._water), 2))

      for n, water in enumerate(self._water):

         # Electric force
         r = water.get_position()-self._charge.get_position()
         r2 = np.sum(np.square(r))
         r = r/np.sqrt(r2)

         a_elec = self._coulomb_constant * self._water_charge * self._charge.charge / (r2 * self._water_mass) * r

         # Cohesive force
         # Lennard-Jones potential is defined as U(r)=4e((s/r)^12-(s/r)^6)
         # Resulting force is radial of norm F = -dU/dr = 4e((12s/r)^13-(6s/r)^7)
         # s is the distance such that U(s)=0 and e the well depth U(r_min)

         for nn, water_bis in enumerate(self._water[n+1:]):

            r = water.get_position() - water_bis.get_position()
            norm_r = np.sqrt(np.sum(np.square(r)))

            if norm_r <= 3 * self._sigma_LJ and norm_r > 0:
               r = r/norm_r
               a = 4 * self._epsilon_LJ / self._water_mass * ((2 * pow(self._sigma_LJ,2))/pow(norm_r,3) - (1 * pow(self._sigma_LJ,1))/pow(norm_r,2)) * r
               
               #3rd Newton's law of reciprocal forces
               a_lejo[n] += a
               a_lejo[n+nn+1] -= a

            
         water.update(self._time_step, a_grav + a_elec + a_lejo[n])
         
         if(n == self._target_drop): 
            ag = np.sqrt(np.sum(np.square(a_grav)))
            ae = np.sqrt(np.sum(np.square(a_elec)))
            al = np.sqrt(np.sum(np.square(a_lejo[n])))
            at = np.sqrt(np.sum(np.square(a_grav + a_elec + a_lejo[n])))
            water.add_acceleration(ag, ae, al, at)

         '''
         print("water drop ", n+1, "out of ", len(self._water))
         print("a_grav = ", a_grav)
         print("a_elec = ", a_elec)
         print("a_lejo = ", a_lejo[n])
         '''

      #if new water should spawn (previous water gone), a line of water is added
      #sum of squares of water coordinates of last spawned batch compared to initial coordinates
      ss = 0
      for nn, water in enumerate(self._water[-self._number_drops:]):
         ss += np.sum(np.square(water.get_position()-self._water_spawn_position[nn]))

      if np.sqrt(ss)/self._number_drops >= self._drop_diameter and self._time[frame] <= self._generation_time: 
         self.new_water()      
      
      return self.update_plot()

   def animate(self, plot_speed_accelaration = 0, save = 0, name_anim = '', name_fig = ''):

      ani = animation.FuncAnimation(self._figure, self.update, frames=len(self._time), interval=int(1000*self._time_step), repeat=False, blit = True)

      if save:

         path = os.path.join(os.path.dirname(__file__), os.pardir)  #parent directory of src
         path = os.path.join(path, 'animations')                    #going into new directory animations
         os.makedirs(path, exist_ok=True)                           #creating new directory animations if needed
         filename = name_anim + '.gif'

         writergif = animation.PillowWriter(fps=int(1//self._time_step))
         ani.save(os.path.join(path, filename), writer=writergif)

         plt.close()

      else: plt.show()

      if plot_speed_accelaration: self._plot_speed_acceleration(save, name_fig)

   def _plot_speed_acceleration(self, save, name):
      
      fig, (ax1, ax2) = plt.subplots(1,2, figsize = (10,5))
      ax1.plot(self._time, self._water[self._target_drop].speed[:len(self._time)])
      ax1.set_ylabel(r'$Vitesse \: [ms^{^-1}]$')
      ax1.set_xlabel(r'Temps [s]')

      ax2.plot(self._time, self._water[self._target_drop].acceleration[:len(self._time)])
      ax2.set_ylabel(r'$Accélération \: [ms^{^-2}]$')
      ax2.set_xlabel(r'Temps [s]')
      ax2.legend(['Gravitation', 'Coulomb', 'Lennard-Jones', 'Total'])

      fig.suptitle("Vitesse et accélération de la goutte n°{} de la première rangée en fonction du temps".format(self._target_drop))

      if save: 
         path = os.path.join(os.path.dirname(__file__), os.pardir)  #parent directory of src
         path = os.path.join(path, 'figures')                       #going into new directory animations
         os.makedirs(path, exist_ok=True)                           #creating new directory animations if needed
         filename = name + '.png'

         plt.savefig(os.path.join(path, filename))

      plt.show()
      plt.close()