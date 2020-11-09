import logging
import sys

from abc import ABC, abstractmethod
import numpy as np

from pyparticles.modules import particle_physics
from pyparticles.modules import particle_env

logger = logging.getLogger(name="PyParticles Main")

def Particle_Motion(ABC):

    def __init__(self,
                 run: str,
                 type: str,
                 **pyparticles_config: Dict[str, object]
                 ):

        # check if defined run is randomized or custom
        if run == 'random':

            self.pyparticles_config = np.random

        elif run == 'custom':

            self.pyparticles_config = pyparticles_config

    # define abstract method for creating particle environments
    @abstractmethod
    def create_environment(self):
        pass

    # define equation(s) of motion for particles
    @abstractmethod
    def equation_of_motion(self):
        pass

# electromagnetic child of generalized particle motion
def Electromagnetic(Particle_Motion):

    def __init__(self):

        super.__init__(self,
                       type='Newtonian')

        # inherit the configuration file for electromagnetic particles
        electro_config = self.pyparticles_config

        # obtain list for particle parameters
        particle_params = electro_config['particle_params']
        time_params = electro_config['time_params']
        vector_conditions = electro_config['vector_conditions']
        integrator_method = electro_config['integrator_method']

        # acquire initial, final, and delta times
        time_i, time_f, dt = time_params[0], time_params[1], time_params[2]

        # acquire particle params
        mass_of_particle, charge_of_particle = particle_params[0], particle_params[1]

        # acquire desired integration method
        integrator_method = electro_config['integrator_method']

        # iterate over each particle in system and gather respective positions, velocities in space
        particle_positions = []
        particle_velocities = []

        for mass, charge in zip(mass_of_particle, charge_of_particle):

            # map the equation of motion to the ode solver
            eom_solve = ode(particle_physics.equation_of_motion()).set_integrator(integrator_method)

            particle_positions.append(particle_physics.compute_particle_trajectory(mass, charge))


def run_create_environment():
    return

def run_particle_trajectories():
    return


def main():

    run_create_environment()

    run_particle_trajectories()

if __name__ == '__main__':

    main()

    exit(main())