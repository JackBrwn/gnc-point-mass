"""
dynamics.py

2-D point mass translational dynamics model

This model implements a discrete time Newtonian dynamics model 
for a planar point mass vehicle. The model propagates position 
and velocity using commanded accelerations in an inertial frame.

Assumptions:
    - Rigid body rotational dynamics neglected
    - Flat Earth, inertial reference frame
    - No aerodynamic or gravitational forces
    - Constant mass
    - Discrete time Euler integration
    
State Vector def:       state = [x, y, vx, vy]

Control input def:      u = [ax, ay]
"""

import numpy as np

def step(state, u, dt):
    
    """
    propagate the state forward one discrete timestep
    
    Parameters
    -----------------
    state : np.ndarray, shape(4,)
        current vehicle state vector:
            state[0] : x-position [m]
            state[1] : y-position [m]
            state[2] : x-velocity [m/s]
            state[3] : y-velocity [m/s]
            
    control : np.ndarray, shape(2,)
        Control input vector
            control[0] : x-acceleration command [m/s^2]
            control[1] : y-acceleration command [m/s^2]
            
    dt : float
        Simulation timestep [s]
        
    Returns
    ----------
    np.ndarray, shape(4,)
        propagated vehicle state at the next timestep
    """
    
    
    x, y, vx, vy = state
    ax, ay = u
    
    x_next = x + vx * dt + 0.5 * ax * dt * dt
    y_next = y + vy *dt  + 0.5 * ay * dt * dt
    vx_next = vx + ax * dt
    vy_next = vy + ay * dt
    
    return np.array([x_next, y_next, vx_next, vy_next])    