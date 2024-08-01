# -*- coding: utf-8 -*-
"""run_Problem2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V4n14w10gjPHAo8EjCwQ3wlYQWZWIOkV
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import skimage
import cv2
from scipy.fftpack import dct

"""### **Problem 2**"""

# Signal

k1, k2, M, N = 10, 8, 48, 32
m, n = np.linspace(0,M-1,num = M), np.linspace(0,N-1,num = N)

cos_k1, cos_k2 = np.meshgrid(np.cos(2*math.pi*k2*n/N),np.cos(2*math.pi*k1*m/M))

x = cos_k1*cos_k2

plt.imshow(x, cmap = 'gray')

# Function to Compute 1D DCT

def DCT_1D(x):

    N = len(x)

    DCT_MAT = np.array([ [ 2 * math.cos((2*n+1)*math.pi*k/(2*N)) for n in range(N) ] for k in range(N) ])

    X = np.matmul(DCT_MAT,x)

    return X

# Function to Compute 2D DCT

def DCT_2D(I):

    row_DCT = DCT_1D(np.transpose(np.array(I)))                                 # Row wise DCT
    DCT_image = DCT_1D(np.transpose(row_DCT))                                   # Column wise DCT

    return DCT_image

plt.imshow(x, cmap = 'gray')
plt.title('Original Image' )
plt.axis('off')

plt.imshow(DCT_2D(x),cmap = 'gray')
plt.title('2D DCT Response (Manual)')
plt.xlabel('$k_2$')
plt.ylabel('$k_1$')

plt.imshow(np.transpose(dct(np.transpose(dct(x)))),cmap = 'gray')
plt.title('2D DCT Response (Library)')
plt.xlabel('$k_2$')
plt.ylabel('$k_1$')

cameraman = skimage.io.imread('/content/cameraman.tif')

plt.imshow(cameraman, cmap = 'gray')
plt.axis('off')

plt.imshow(np.log(np.abs(DCT_2D(cameraman))), cmap = 'gray')
plt.title('2D DCT Response (Manual)')
plt.ylabel('$k_1$')
plt.xlabel('$k_2$')