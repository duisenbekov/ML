from scipy import linalg
import math
from numpy.linalg import inv
import numpy as np
from scipy.optimize import minimize as min
F = lambda x: np.sin(x / 5.0) * np.exp(x / 10.0) + 5 * np.exp(-x / 2.0)
X= np.arange (1, 15, 0.1)
a = min(f, 2, method='BFGS')

