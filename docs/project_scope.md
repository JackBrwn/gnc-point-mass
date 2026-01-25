Project Scope — 2-D Point-Mass GNC Simulation (Python + LQR)
Objective

Develop and validate a software-based Guidance, Navigation, and Control (GNC) system for a planar point-mass vehicle using Python, simulated sensors, LQR feedback control, and state estimation via a discrete Kalman filter.

System Description

The system is modeled as a two-dimensional point-mass vehicle moving in the horizontal plane. Only translational position and velocity states are considered. Rotational dynamics, aerodynamics, and attitude effects are neglected.

State Definition

The state vector is defined as:

x = [x, y, v_x, v_y]^T

where:

x, y : planar position

v_x, v_y : planar velocity

Control Inputs

The control input vector is:

u = [a_x, a_y]^T

where:

a_x, a_y : commanded accelerations in the inertial frame

Control inputs are subject to saturation limits representing actuator constraints.

System Dynamics

The vehicle dynamics follow Newtonian point-mass equations:

dx/dt = v_x
dy/dt = v_y
dv_x/dt = a_x
dv_y/dt = a_y

The system will be implemented in discrete time with a fixed simulation timestep. Python’s numpy will be used for matrix operations.

Sensor Models

Simulated sensors provide noisy measurements of selected states:

Position measurements (like GPS)

Optional velocity measurements

Sensor models include:

Additive zero-mean Gaussian noise

Optional constant or slowly varying bias

Independent sensor sampling rate

Disturbances

External disturbances will be applied to evaluate robustness, including:

Step disturbances

Constant acceleration biases

Impulse disturbances

Control Architecture

The controller will use Linear Quadratic Regulator (LQR) feedback control:

Designed using the state-space model of the vehicle

Stabilizes the system and tracks reference trajectories

Rejects disturbances

Performance evaluated using standard time-domain metrics (settling time, overshoot, control effort)

State Estimation

A discrete Kalman filter will estimate the vehicle state from noisy sensor measurements:

Uses the same physics-based model as the controller

Incorporates process noise (Q) to account for uncertainty

Measurement noise covariance (R) models sensor noise

Estimated states are used for feedback control

Simulation Phases

The project includes:

Open-loop simulation without control

Closed-loop simulation using true states

Closed-loop simulation using estimated states only (Kalman filter output)

Performance Evaluation

System performance will be evaluated by:

Tracking error relative to reference

Stability and damping behavior

Control effort and actuator saturation

Estimation error statistics

Deliverables

The final project will include:

Modular Python code (src/) implementing dynamics, sensors, LQR controller, and Kalman filter

Plots demonstrating system behavior, tracking, and estimation performance (plots/)

Block diagram of the full G-N-C loop (docs/block_diagram.png)

Written documentation summarizing assumptions, methods, and results (docs/project_scope.md)