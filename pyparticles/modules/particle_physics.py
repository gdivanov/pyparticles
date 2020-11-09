import numpy as np
from scipy.integrate import ode

GRAVITATIONAL_CONST = 6.67408 * 10 ** -11  # in m3 kg-1 s-2
ELECTRON_CHARGE = 1.60217662 * 10 ** -19  # in coulombs
ELECTRON_REST_MASS = 9.10938356 * 10 ** -31  # in kg


# e.o.m. set up
def equation_of_motion(mass_of_particle: float,
                       charge_of_particle: float,
                       position_vector: np.array,
                       velocity_vector: np.array,
                       magnetic_magnitude: float,
                       electric_magnitude: float,
                       eom_solve: object
                       ) -> np.array:
    """

    Parameters
    ----------
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

    # acquire particle params
    mass_of_particle, charge_of_particle = particle_params[0], particle_params[1]

    # acquire particle params
    electric_magnitude, magnetic_magnitude = electromagnetic_params[0], electromagnetic_params[1]

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


# o.d.e. solver for trajectory calculation
def compute_particle_trajectory(time_i: float,
                                time_f: float,
                                dt: float,
                                mass_of_particle: float,
                                charge_of_particle: float,
                                position_vector: np.array,
                                velocity_vector: np.array) -> np.array:
    """

    Parameters
    ----------
    time_params (np.array) : initial, final, and time step (s)
    particle_params (np.array) : mass and charge of particle (kg : coulombs)
    vector_conditions_i (np.array) : initial conditions of particle (position : velocity)
    integrator_method (str) : type of integration to use
    equation_of_motion (object) : eom function

    Returns
    -------
    position, velocity (tuple([])) : tuple of positions and velocities of particle across space

    """

    # apply given initial conditions of the system to the mapper
    eom_solve.set_initial_value(vector_conditions_i, time_i).set_f_params(mass_of_particle, charge_of_particle, 1.0,
                                                                          10.0)

    # create positions list for particle's trajetory and velocity in space
    particle_positions = []
    particle_velocities = []

    # run through path of particle by integrating over the time steps til final time is reached
    while eom_solve.successful() and eom_solve.t < time_f:
        eom_solve.integrate(eom_solve.t + dt)

        particle_positions.append(eom_solve.y[:3])
        particle_velocities.append(eom_solve.y[3:])

    return np.array(particle_positions), np.array(particle_velocities)
