import numpy as np


def zero_disturbance(t = None):
    return np.array([0, 0])

    
def step_disturbance(t, t_on = 60, t_off = 120, d_on = None):
    
    if d_on is None:
        return np.array([0, 0])
    
    if t_on <= t < t_off:
        return d_on
    else:
        return np.array([0, 0])

  
def impulse_disturbance(t, dt, t_impulse, impulse):
    
    if abs(t - t_impulse) < dt:
        return impulse
    else:
        return np.array([0,0])


def bias_disturbance(bias):
    return bias

    
def random_disturbance(sigma):
    return np.random.normal(0, sigma, size = 2)