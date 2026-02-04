import numpy as np
import matplotlib.pyplot as plt

def plot_results(history, measured_history, dt, num_steps, zoom_steps=200):
    """
    Generate industry-style plots for 2-D point mass simulation including positions and velocities.

    Parameters
    ----------
    history : np.ndarray, shape (num_steps+1, 4)
        True vehicle state history [x, y, vx, vy]
        
    measured_history : np.ndarray, shape (num_steps+1, 4)
        Noisy measured state history [x, y, vx, vy]
        
    dt : float
        Simulation timestep [s]
        
    num_steps : int
        Number of simulation steps
        
    zoom_steps : int
        Number of timesteps to zoom in on for error readability
    """
    
    # Time array
    t = np.arange(0, (num_steps+1)*dt, dt)
    
    # --- Errors ---
    error_x = measured_history[:,0] - history[:,0]
    error_y = measured_history[:,1] - history[:,1]
    error_total_pos = np.sqrt(error_x**2 + error_y**2)

    error_vx = measured_history[:,2] - history[:,2]
    error_vy = measured_history[:,3] - history[:,3]
    error_total_vel = np.sqrt(error_vx**2 + error_vy**2)
    
    # --- Create 2x3 subplot layout ---
    fig, axs = plt.subplots(2, 3, figsize=(18,10))
    
    # --- 1. X-position vs time ---
    axs[0,0].plot(t, history[:,0], label='x (true)')
    axs[0,0].plot(t, measured_history[:,0], label='x (measured)', alpha=0.7)
    axs[0,0].set_xlabel('Time [s]')
    axs[0,0].set_ylabel('X position [m]')
    axs[0,0].set_title('X-position vs Time')
    axs[0,0].legend()
    axs[0,0].grid(True)
    
    # --- 2. Y-position vs time ---
    axs[0,1].plot(t, history[:,1], label='y (true)')
    axs[0,1].plot(t, measured_history[:,1], label='y (measured)', alpha=0.7)
    axs[0,1].set_xlabel('Time [s]')
    axs[0,1].set_ylabel('Y position [m]')
    axs[0,1].set_title('Y-position vs Time')
    axs[0,1].legend()
    axs[0,1].grid(True)
    
    # --- 3. 2-D Trajectory ---
    axs[0,2].plot(history[:,0], history[:,1], label='True trajectory')
    axs[0,2].plot(measured_history[:,0], measured_history[:,1], label='Measured trajectory', alpha=0.7)
    axs[0,2].set_xlabel('X position [m]')
    axs[0,2].set_ylabel('Y position [m]')
    axs[0,2].set_title('2-D Vehicle Trajectory')
    axs[0,2].legend()
    axs[0,2].grid(True)
    axs[0,2].axis('equal')  # maintain X/Y scale ratio
    
    # --- 4. Measurement errors (position, zoomed) ---
    axs[1,0].plot(t[:zoom_steps], error_x[:zoom_steps], label='x error', alpha=0.7)
    axs[1,0].plot(t[:zoom_steps], error_y[:zoom_steps], label='y error', alpha=0.7)
    axs[1,0].plot(t[:zoom_steps], error_total_pos[:zoom_steps], label='total error', linestyle='--', color='k')
    axs[1,0].set_xlabel('Time [s]')
    axs[1,0].set_ylabel('Position error [m]')
    axs[1,0].set_title(f'Position Errors (first {zoom_steps} timesteps)')
    axs[1,0].legend()
    axs[1,0].grid(True)
    
    # --- 5. Velocity vs time ---
    axs[1,1].plot(t, history[:,2], label='vx (true)')
    axs[1,1].plot(t, measured_history[:,2], label='vx (measured)', alpha=0.7)
    axs[1,1].plot(t, history[:,3], label='vy (true)')
    axs[1,1].plot(t, measured_history[:,3], label='vy (measured)', alpha=0.7)
    axs[1,1].set_xlabel('Time [s]')
    axs[1,1].set_ylabel('Velocity [m/s]')
    axs[1,1].set_title('Velocity vs Time')
    axs[1,1].legend()
    axs[1,1].grid(True)
    
    # --- 6. Measurement errors (velocity, zoomed) ---
    axs[1,2].plot(t[:zoom_steps], error_vx[:zoom_steps], label='vx error', alpha=0.7)
    axs[1,2].plot(t[:zoom_steps], error_vy[:zoom_steps], label='vy error', alpha=0.7)
    axs[1,2].plot(t[:zoom_steps], error_total_vel[:zoom_steps], label='total error', linestyle='--', color='k')
    axs[1,2].set_xlabel('Time [s]')
    axs[1,2].set_ylabel('Velocity error [m/s]')
    axs[1,2].set_title(f'Velocity Errors (first {zoom_steps} timesteps)')
    axs[1,2].legend()
    axs[1,2].grid(True)
    
    plt.tight_layout()
    plt.show()
    
    # --- Optional: Histograms ---
    plt.figure(figsize=(10,6))
    plt.hist(error_x, bins=30, alpha=0.7, label='x position error')
    plt.hist(error_y, bins=30, alpha=0.7, label='y position error')
    plt.hist(error_vx, bins=30, alpha=0.7, label='vx error')
    plt.hist(error_vy, bins=30, alpha=0.7, label='vy error')
    plt.xlabel('Error')
    plt.ylabel('Count')
    plt.title('Histogram of Position and Velocity Errors')
    plt.legend()
    plt.grid(True)
    plt.show()
