# chapter 2. Perceptron - 예제 모음
#
# runnable 
# %run C:\Users\Administrator\Documents\workspace\deep_learing_for_scratch\perceptron_ex1.py

import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])

b = -0.7
c = w*x

np.sum(c)

np.sum(w*x) + b