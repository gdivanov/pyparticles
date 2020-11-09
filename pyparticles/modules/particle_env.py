import numpy as np


def e_field_sign(particle_position: int):
    direction_of_field = 12 * np.sign(np.sin(2 * np.pi * particle_position / 15))
    return direction_of_field


def b_field_sign(particle_position: int):
    return

def generate_environment(environment_size: np.array) -> np.array:
    return generated_environment
