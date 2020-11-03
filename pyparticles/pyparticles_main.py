import logging
import sys

from abc import ABC, abstractmethod
import numpy as np

from pyparticles.modules import particle_physics
from pyparticles.modules import particle_env

logger = logging.getLogger(name="PyParticles Main")

def Particle_Motion(ABC):

    def __init__(self,
                 run_type: str,
                 **pyparticles_config: Dict[str, object]
                 ):

        if run_type == 'random':

            self.pyparticles_config = np.random

        elif run_type == 'custom':

            self.pyparticles_config = pyparticles_config

    @abstractmethod
    def create_environment(self):

    @abstractmethod
    def equation_of_motion(self):


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