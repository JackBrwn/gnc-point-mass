import matplotlib.pyplot as plt
import numpy as np
import os

def plot_results(results, reference_state=None, u_limits=None):
    """
    Plot GNC simulation results.
    
    Parameters
    ----------
    results : dict
        Dictionary returned by run_simulation()
        Keys: 'time', 'true', 'measured', 'estimated', 'control', 'metrics'
    reference_state : np.ndarray, optional
        Reference position [x, y] for plotting
    u_limits : tuple, optional
        (u_min, u_max) for plotting actuator limits
    """
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    save_dir = os.path.join(project_root, 'plots')
    os.makedirs(save_dir, exist_ok = True)
    
    t = results['time']
    true = results['true']
    measured = results['measured']
    estimated = results['estimated']
    control = results['control']

    # ----------------------
    # 1. True vs Measured States
    # ----------------------
    fig, axs = plt.subplots(2,1, figsize=(10,6), sharex=True)
    axs[0].plot(t, true[:,0], label='True x')
    axs[0].plot(t, measured[:,0], '--', label='Measured x')
    axs[0].set_ylabel('X Position [m]')
    axs[0].legend()
    axs[0].grid(True)
    
    axs[1].plot(t, true[:,1], label='True y')
    axs[1].plot(t, measured[:,1], '--', label='Measured y')
    axs[1].set_ylabel('Y Position [m]')
    axs[1].set_xlabel('Time [s]')
    axs[1].legend()
    axs[1].grid(True)
    plt.suptitle('True vs Measured States')
    plt.show()
    fig.savefig(os.path.join(save_dir, 'true_vs_measured.png'))

    # ----------------------
    # 2. True vs Estimated States
    # ----------------------
    fig, axs = plt.subplots(2,1, figsize=(10,6), sharex=True)
    axs[0].plot(t, true[:,0], label='True x')
    axs[0].plot(t, estimated[:,0], '--', label='Estimated x')
    axs[0].set_ylabel('X Position [m]')
    axs[0].legend()
    axs[0].grid(True)
    
    axs[1].plot(t, true[:,1], label='True y')
    axs[1].plot(t, estimated[:,1], '--', label='Estimated y')
    axs[1].set_ylabel('Y Position [m]')
    axs[1].set_xlabel('Time [s]')
    axs[1].legend()
    axs[1].grid(True)
    plt.suptitle('True vs Estimated States')
    plt.show()
    fig.savefig(os.path.join(save_dir, 'true_vs_estimated.png'))

    # ----------------------
    # 3. Estimation Error
    # ----------------------
    error = true - estimated
    fig, axs = plt.subplots(2,1, figsize=(10,6), sharex=True)
    axs[0].plot(t, error[:,0], label='X Error')
    axs[0].set_ylabel('X Error [m]')
    axs[0].legend()
    axs[0].grid(True)
    
    axs[1].plot(t, error[:,1], label='Y Error')
    axs[1].set_ylabel('Y Error [m]')
    axs[1].set_xlabel('Time [s]')
    axs[1].legend()
    axs[1].grid(True)
    plt.suptitle('Estimation Error vs Time')
    plt.show()
    fig.savefig(os.path.join(save_dir, 'estimated_error_vs_time.png'))


    # ----------------------
    # 4. Control Inputs vs Limits
    # ----------------------
    fig, axs = plt.subplots(2,1, figsize=(10,6), sharex=True)
    axs[0].plot(t, control[:,0], label='Control X')
    if u_limits is not None:
        u_min, u_max = u_limits
        axs[0].axhline(u_min, color='r', linestyle='--', label='u_min')
        axs[0].axhline(u_max, color='g', linestyle='--', label='u_max')
    axs[0].set_ylabel('Control X [m/s²]')
    axs[0].legend()
    axs[0].grid(True)
    
    axs[1].plot(t, control[:,1], label='Control Y')
    if u_limits is not None:
        axs[1].axhline(u_min, color='r', linestyle='--', label='u_min')
        axs[1].axhline(u_max, color='g', linestyle='--', label='u_max')
    axs[1].set_ylabel('Control Y [m/s²]')
    axs[1].set_xlabel('Time [s]')
    axs[1].legend()
    axs[1].grid(True)
    plt.suptitle('Control Input vs Limits')
    plt.show()
    fig.savefig(os.path.join(save_dir, 'control_input_vs_limits.png'))

    # ----------------------
    # 5. Reference Tracking
    # ----------------------
    if reference_state is not None:
        fig, ax = plt.subplots(figsize=(6,6))
        ax.plot(true[:,0], true[:,1], label='True Trajectory')
        ax.plot(estimated[:,0], estimated[:,1], '--', label='Estimated Trajectory')
        ax.plot(reference_state[0], reference_state[1], 'ro', label='Reference')
        ax.set_xlabel('X Position [m]')
        ax.set_ylabel('Y Position [m]')
        ax.set_title('Reference Tracking')
        ax.legend()
        ax.grid(True)
        plt.show()
        fig.savefig(os.path.join(save_dir, 'reference_tracking.png'))
