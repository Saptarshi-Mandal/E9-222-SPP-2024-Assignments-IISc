# -*- coding: utf-8 -*-
"""run_Problem1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e4zFmiodBlhGcOqu2hkKyJH6t6BLafjx
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

"""### **Problem 1**"""

# Function to Compute 1D DCT

def DCT_1D(x):

    N = len(x)

    DCT_MAT = np.array([ [ 2 * math.cos((2*n+1)*math.pi*k/(2*N)) for n in range(N) ] for k in range(N) ]) # DCT Matrix

    X = np.matmul(DCT_MAT,x)

    return X

# Signal
k0, N = 5, 32
n = np.linspace(0,N-1,num = N)
x = np.cos(2*math.pi*k0*n/N)

plt.stem(x,'r')
plt.title('$x[n]$')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.stem(DCT_1D(x))
plt.title('$X[k]$ (DCT Manual Implementation)')
plt.xlabel('k')
plt.ylabel('Magnitude')

plt.stem(scipy.fftpack.dct(x))
plt.title('$X[k]$ (DCT Library Implementation)')
plt.xlabel('k')
plt.ylabel('Magnitude')