# -*- coding: utf-8 -*-
"""run_Problem1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NstdMMUXON3znvwDF_yK2PvL2FZg0W--
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
import math

# Time specification
T = [0.001, 0.01, 0.1, 1]; # Time Step Sizes

"""### **x_1(t)**"""

# 1) x_1(t)
plot_number=1
plt.figure(figsize = (20,25))
plt.suptitle('$x_1(t)$', size = 24)
for time_step in T:                                                             # Different Samplings
    t = np.arange(-5,5+time_step,time_step)                                     # Time
    for sigma_sq in [0.1,1]:
        plt.subplot(4,2,plot_number)
        plt.stem(t, np.exp((-t**2)/(2*sigma_sq)),basefmt='')                    # Plotting the function
        plt.title(f'T : {time_step}  and sigma_sq : {sigma_sq}')           # Sub Plot Title
        plt.xlabel('Time (in seconds)')                                         # X axis label
        plt.ylabel('Amplitude')                                                 # Y axis label
        plot_number= plot_number + 1                                            # Incrementing plot number
plt.show()

"""### **x_2(t)**"""

# 2) x_2(t)
plot_number = 1
plt.figure(figsize = (20,25))
plt.suptitle('$x_2(t)$', size = 24)
for time_step in T:
    t = np.arange(-5,5+time_step,time_step)
    plt.subplot(4,1,plot_number)
    plt.stem(t, np.exp(-abs(t)),basefmt='')                                     # plot the function
    plt.title(f'T : {time_step}')                                       # subplot title
    plt.xlabel('Time (in seconds)')                                             # X axis label
    plt.ylabel('Amplitude')                                                     # Y axis label
    plot_number= plot_number + 1                                                # Incrementing plot number
plt.show()

"""### **x_3(t)**"""

# 3) x_3(t)
plot_number = 1
alpha = -0.02
w_0 = 2*math.pi*200
plt.figure(figsize = (20,20))
plt.suptitle('$x_3(t)$', size = 24)
for time_step in T:
    t = np.arange(-5,5+time_step,time_step);
    plt.subplot(4,1,plot_number)
    plt.plot(t, np.exp(alpha*t)*np.cos(w_0*t)*(t>0))                            # plotting the function
    plt.title(f'T : {time_step}')                                               # subplot title
    plt.xlabel('Time (in seconds)')                                             # X axis label
    plt.ylabel('Amplitude')                                                     # Y axis label
    plot_number= plot_number + 1                                                # Incrementing plot number
plt.show()

