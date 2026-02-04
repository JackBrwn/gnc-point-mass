import numpy as np
import matplotlib.pyplot as plt

from dynamics import step
from sensors import sensor_model as senm
from visualize import plot_results

state = np.array([0, 0, 0, 0])
dt = 0.1
t_total = 60 * 5
num_steps = round(t_total / dt)

history = np.zeros((num_steps+1, state.size))
measured_history = np.zeros((num_steps+1, state.size))
history[0] = state
measured_history[0] = senm(state)

u = np.array([0.5, 0.5])

for k in range(num_steps):
    
    state = step(state, u, dt)
    history[k+1] = state   
    measured_history[k+1] = senm(state)

plot_results(history, measured_history, dt, num_steps)

