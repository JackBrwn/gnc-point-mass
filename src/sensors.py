"""
sensors.py

2-D point mass position and velocity sensor model

This model implements normally distributed Gaussian 
noise centered around the true state.

State Vector def:       state = [x, y, vx, vy]

Position sensor noise:  sigma_pos = float

Velocity sensor noise:  sigma_vel = float
"""

import numpy as np

def sensor_model(state, sigma_pos=0.5, sigma_vel=0.1):
    
    """
    adds sensor noise to the state
    
    Parameters
    --------------
    state : np.ndarray, shape(4,)
        current vehicle state vector:
            state[0] : x-position [m]
            state[1] : y-position [m]
            state[2] : x-velocity [m/s]
            state[3] : y-velocity [m/s]
            
    sigma_pos : float
        Position sensor noise [m]
        
    sigma_vel : float
        Velocity sensor noise [m/s]
        
    Returns
    -----------
    np.ndarray, shape(4,)
        noisy vehicle state
    """
    
    x_measured = state[0] + np.random.normal(0, sigma_pos)
    y_measured = state[1] + np.random.normal(0, sigma_pos)
    vx_measured = state[2] + np.random.normal(0, sigma_vel)
    vy_measured = state[3] + np.random.normal(0, sigma_vel)
    
    return np.array([x_measured, y_measured, vx_measured, vy_measured])
    