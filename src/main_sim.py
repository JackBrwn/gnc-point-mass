import numpy as np
import matplotlib.pyplot as plt

from dynamics import step

state = np.array([0, 0, 0, 0])
dt = 0.1
t_total = 60 * 5
num_steps = round(t_total / dt)

history = np.zeros((num_steps+1, state.size))
history[0] = state

u = np.array([0.5, 0.5])

for k in range(num_steps):
    
    state = step(state, u, dt)
    history[k+1] = state   


print(history)