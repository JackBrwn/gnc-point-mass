import numpy as np
from dynamics import step
from sensors import sensor_model
from controller import PID_controller
from kalman import kalman_filter_step
from disturbance_profiles import zero_disturbance
from disturbance_profiles import step_disturbance
from disturbance_profiles import impulse_disturbance
from disturbance_profiles import bias_disturbance
from disturbance_profiles import random_disturbance

def run_simulation(reference_state=np.array([5,5]),
                   dt=0.1,
                   t_total=120,
                   sensor_noise=(0.5, 0.1),
                   process_noise_Q=None,
                   controller_params={'Ts':2.5,'zeta':0.7,'u_max':5,'u_min':-5,'tau':0.2},
                   disturbance_fn=zero_disturbance):
    """
    Run a full 2D point-mass GNC simulation.
    
    Returns:
        results : dict
            Contains time array, true states, measured states,
            estimated states, control inputs, and metrics
    """
    
    # Simulation setup
    num_steps = round(t_total / dt)
    t_array = np.arange(0, t_total+dt, dt)
    
    # Initialize states
    state = np.zeros(4)           # [x, y, vx, vy]
    x_hat = state.copy()          # KF estimate
    P = np.diag([1,1,1,1])
    int_error = np.zeros(2)
    u_actual = np.zeros(2)
    
    # Histories
    history = np.zeros((num_steps+1, 4))
    measured_history = np.zeros((num_steps+1, 4))
    estimated_history = np.zeros((num_steps+1, 4))
    control_history = np.zeros((num_steps+1, 2))
    
    history[0] = state
    measured_history[0] = sensor_model(state, *sensor_noise)
    estimated_history[0] = x_hat
    control_history[0] = u_actual
    
    # Process noise
    if process_noise_Q is None:
        Q = np.diag([1e-4, 1e-4, 1e-3, 1e-3])
    else:
        Q = process_noise_Q
    
    # Main loop
    for k in range(num_steps):
        t = t_array[k]
        
        # Controller
        u_desired, int_error = PID_controller(
            dt,
            x_hat,
            reference_state,
            int_error,
            controller_params['Ts'],
            controller_params['zeta'],
            u_actual,
            controller_params['u_max'],
            controller_params['u_min']
        )
        u_actual = u_desired
        
        # Disturbance
        d = disturbance_fn(t)
        
        # Dynamics update
        state = step(state, u_actual + d, dt)
        history[k+1] = state
        
        # Sensor measurement
        measured_state = sensor_model(state, *sensor_noise)
        measured_history[k+1] = measured_state
        
        # Kalman filter update
        x_hat, P = kalman_filter_step(x_hat, P, u_actual, measured_state, dt=dt, Q=Q)
        estimated_history[k+1] = x_hat
        
        # Store control
        control_history[k+1] = u_actual
    
    # Compute metrics
    pos_error = history[:, :2] - reference_state[:2]
    error_norm = np.linalg.norm(pos_error, axis=1)
    tol = 0.02 * np.linalg.norm(reference_state[:2])
    settling_time = t_total
    for k in range(len(error_norm)):
        if np.all(error_norm[k:] <= tol):
            settling_time = t_array[k]
            break
    
    pos_norm = np.linalg.norm(history[:, :2], axis=1)
    ref_norm = np.linalg.norm(reference_state[:2])
    overshoot_percent = (np.max(pos_norm) - ref_norm) / ref_norm * 100
    rmse = np.sqrt(np.mean((history[:,:2] - estimated_history[:,:2])**2))
    u_max_vals = np.max(control_history, axis=0)
    u_min_vals = np.min(control_history, axis=0)
    
    metrics = {
        'settling_time': settling_time,
        'overshoot_percent': overshoot_percent,
        'error_norm': error_norm,
        'rmse': rmse,
        'u_max': u_max_vals,
        'u_min': u_min_vals
    }
    
    results = {
        'time': t_array,
        'true': history,
        'measured': measured_history,
        'estimated': estimated_history,
        'control': control_history,
        'metrics': metrics
    }
    
    return results
