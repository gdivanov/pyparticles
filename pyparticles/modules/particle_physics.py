import numpy as np
from scipy.integrate import ode

GRAVITATIONAL_CONST = 6.67408 * 10 ** -11  # in m3 kg-1 s-2
ELECTRON_CHARGE = 1.60217662 * 10 ** -19  # in coulombs
ELECTRON_REST_MASS = 9.10938356 * 10 ** -31  # in kg

def equation_of_motion(t: float,
                       mass_of_particle: float,
                       charge_of_particle: float,
                       position_vector: np.array,
                       velocity_vector: np.array,
                       magnetic_magnitude: float,
                       electric_magnitude: float
                       ) -> np.array:
    """

    Parameters
    ----------
    t (float) : time (s)
    mass_of_particle (float) : particle's mass (kg)
    charge_of_particle (float) : particle's electromagnetic charge (coloumbs)
    position_vector (np.array) : x, y, z positions of particle at time t
    velocity_vector (np.array) : angular, radial, rotational velocities of particle at time t
    magnetic_magnitude (float) : magnetic field magnitude at position x, y, z at time t
    electric_magnitude (float) : electric field magnitude at position x, y, z at time t

    Returns
    -------
    dx_dt (np.array) : derivative output array to calculate solution to o.d.e.

    """

    # acquire all velocity values
    x_velocity = velocity_vector[0]
    y_velocity = velocity_vector[1]
    angular_velocity = velocity_vector[2]

    # corner cases of when electric/magnetic magnitudes are nonetype
    if electric_magnitude is None:
        electric_magnitude = 0.0

    if magnetic_magnitude is None:
        magnetic_magnitude = 1.0

    # TODO: change names of velocities and dx_dt to more clearly defined things
    # calculate the acceleration in the angular direction
    angular_acceleration = (charge_of_particle / mass_of_particle) * magnetic_magnitude

    # parse together derivative array to calculate o.d.e. on
    dx_dt = np.array([x_velocity, y_velocity, angular_velocity, 0,
                      angular_acceleration * angular_velocity + electric_magnitude,
                      -angular_acceleration * y_velocity])

    return dx_dt
