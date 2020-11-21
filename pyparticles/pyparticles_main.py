import logging
import sys, os

from abc import ABC, abstractmethod
from typing import Dict
import numpy as np

from modules import particle_physics
from modules import particle_env
from modules import utils

logger = logging.getLogger(name="PyParticles Main")

class ParticleMotion(ABC):

    def __init__(self,
                 pyparticles_config: Dict[str, object]
                 ):

        if pyparticles_config is not None:
            self.run = pyparticles_config['run_params']['run_type']
        else:
            self.run = None

        # check if defined run is randomized or custom
        if self.run == 'random':

            self.pyparticles_config = np.random
            self.physics = np.random
            self.type = np.random

        elif self.run == 'custom':

            self.pyparticles_config = pyparticles_config
            self.physics = self.pyparticles_config['environment_params']['physics']
            self.type = self.pyparticles_config['environment_params']['type']

    # TODO: create responsive environment creation methodology to build in
    # define abstract method for creating particle environments
    @abstractmethod
    def create_environment(self):
        pass

    # define equation(s) of motion for particles
    @abstractmethod
    def equation_of_motion(self):
        pass

# electromagnetic child of generalized particle motion
class Electromagnetic(ParticleMotion):

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
        mass_of_particles, charge_of_particles = particle_params[0], particle_params[1]

        # acquire desired integration method
        integrator_method = electro_config['integrator_method']

    def create_environment(self):
        return created_environment

    def equation_of_motion(self,
                           mass_of_particles: list,
                           charge_of_particles: list,
                           time_i: float,
                           time_f: float,
                           dt: float,
                           integrator_method: str) -> list:

        # iterate over each particle in system and gather respective positions, velocities in space
        particle_positions = []
        particle_velocities = []

        for mass, charge in zip(mass_of_particles, charge_of_particles):

            # map the equation of motion to the ode solver
            eom_solve = ode(particle_physics.equation_of_motion()).set_integrator(integrator_method)

            particle_positions.append(particle_physics.compute_particle_trajectory(mass, charge))

        return particle_positions, particle_velocities

def run_read_config():

    abspath = os.path.abspath(__file__)
    current_path = os.path.dirname(abspath)

    # get path to general config file
    config_path = os.path.join(
        current_path, os.path.join("resources", "config.yml")
    )

    return utils.process_yaml(file_path=config_path, read_write_type='r')


def run_particle_trajectories(pyparticles_config: dict):

    # instantiate main abstract class
    ParticleMotion(pyparticles_config=pyparticles_config)

    # check for the physics type to run on (Electromagnetic, Thermal/Pressure, etc..)
    if pyparticles_config['physical_system'] == 'Electromagnetic':

        particle_positions, particle_velocities = Electromagnetic(ParticleMotion)

    return particle_positions, particle_velocities

def main():

    # read in main config yaml
    pyparticles_config = run_read_config()

    # run through particle trajectories and velocities in space
    particle_positions, particle_velocities = run_particle_trajectories(pyparticles_config=pyparticles_config)

if __name__ == '__main__':

    main()

    exit(main())