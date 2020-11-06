import logging
import sys

from abc import ABC, abstractmethod
import numpy as np

from pyparticles.modules import particle_physics
from pyparticles.modules import particle_env

logger = logging.getLogger(name="PyParticles Main")

def ParticleMotion(ABC):

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
def Electromagnetic(ParticleMotion):

    def __init__(self):

        super.__init__(self,
                       type='Newtonian')

        # inherit the configuration file for electromagnetic particles
        electro_config = self.pyparticles_config

        # obtain list for particle parameters
        particle_params = electro_config['particle_params']

        # run over positions of particle(s)



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