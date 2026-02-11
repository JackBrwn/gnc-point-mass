import numpy as np

def PD_controller(dt, state, reference_state, Ts, zeta, u_actual, u_max, u_min):
    
    wn = 4 / Ts / zeta
    
    kp = wn * wn
    kd = 2 * wn * zeta
    
    pos_error = reference_state[:2] - state[:2]
    vel_error = -state[2:]
    
    tau = 0.2
    u_desired = kp * pos_error + kd * vel_error
    u_actual = u_actual + (u_desired - u_actual)*dt/tau
    
    return np.clip(u_actual, u_min, u_max)
    
    
def PID_controller(dt, state, reference_state, int_error, Ts, zeta, u_actual, u_max, u_min):
    
    wn = 4 / Ts / zeta
    
    kp = wn * wn
    ki = 0.105 * kp
    kd = 2 * wn * zeta
    
    pos_error = reference_state[:2] - state[:2]
    vel_error = -state[2:]
    int_error = int_error + pos_error * dt
    
    int_error_max = u_max / ki
    int_error = np.clip(int_error, -int_error_max, int_error_max)
    
    tau = 0.2
    u_desired = kp * pos_error + ki * int_error + kd * vel_error
    u_actual = u_actual + (u_desired - u_actual)*dt/tau
    
    return np.clip(u_actual, u_min, u_max), int_error