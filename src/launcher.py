import numpy as np
from main_sim import run_simulation
from visualize import plot_results

results = run_simulation()
plot_results(results, reference_state = np.array([5, 5]), u_limits = (-5, 5))