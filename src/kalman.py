import numpy as np

def kalman_filter_step(x_hat, P, u, measured_state, dt, Q):
    
    A = np.array([[1, 0, dt, 0],
                  [0, 1, 0, dt],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])
    B = np.array([[0.5*dt**2, 0],
                  [0, 0.5*dt**2],
                  [dt, 0],
                  [0, dt]])
    H = np.eye(4)
    R = np.diag([0.05**2, 0.05**2, 0.02**2, 0.02**2])
    I = np.eye(4)
    
    x_pred = A @ x_hat + B @ u
    P_pred = A @ P @ A.T + Q
    
    y = measured_state - H @ x_pred
    S = H @ P_pred @ H.T + R
    K = P_pred @ H.T @ np.linalg.inv(S)

    x_new = x_pred + K @ y
    P_new = (I - K @ H) @ P_pred

    return x_new, P_new   
    