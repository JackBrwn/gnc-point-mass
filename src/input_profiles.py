import numpy as np

def zero_input():
    return np.array([0, 0])

def step_input(t, t_on = 30, t_off = 90, u_on = None):
    
    if u_on is None:
        return np.array([0, 0])
    
    if t_on <= t < t_off:
        return u_on
    else:
        return np.array([0, 0])
    
def sinusoidal_input(t, amplitude = np.array([0.5, 0.5]), frequency = np.array([0.2, 0.2])):
    return np.array([amplitude[0]*np.sin(2*np.pi*frequency[0]*t), amplitude[1]*np.cos(2*np.pi*frequency[1]*t)])