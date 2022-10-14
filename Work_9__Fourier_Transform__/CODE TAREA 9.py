# -*- coding: utf-8 -*-
"""TAREA 9 | Transformada de Fourier .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iO7TI-r42VcwxI8-DEa_aCUisypk9Qpz
"""

# LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# READ AND SHOW IMAGE 1
img = cv.imread('/content/Fig0409(a).tif', 0)
plt.imshow(img, 'gray')
plt.show()

# INVERSE FAST FOURIER TRANSFORM 
def ifft2(A, B):
  return np.fft.ifft2(A * np.exp(1j*B))

# FUNCTION TO PLOT IMAGE AND SAVE PNG
def plot_img(img, title, name, min, max):

  plt.title(title)
  if min == max:
    plt.imshow(img, 'gray')  
  else:
    plt.imshow(img, 'gray', vmin=min, vmax=max)
  cv.imwrite('/content/Results/'+name+'.png', img)

  plt.show()

# FAST FOURIER TRANSFORMATION, MAGNITUDE AND ANGLE (PHASE)
fft_img = np.fft.fft2(img)
mag_fft_img = abs(fft_img)
phase_fft_img = np.angle(fft_img)

# CREATING IMAGE 2 COLOR BLACK WITH A WHITE RECTANGLE IN THE CENTER
img2 = np.zeros(np.shape(img))
x = np.shape(img)[0] // 2
y = np.shape(img)[1] // 2
img2[x - 100:x + 101,y - 25:y + 26] = 255

# SHOW IMAGE 2
plot_img(img2, 'Image 2', 'img2', 0, 0)

# FAST FOURIER TRANSFORM TO IMAGE 2, MAGNITUD AND PHASE
fft_img2 = np.fft.fft2(img2)
mag_fft_img2 = abs(fft_img2)
phase_fft_img2 = np.angle(fft_img2)

# MATRIX OF ONES VALUES AND OTHER WITH PI/2 VALUES
mag_ones = np.ones(np.shape(img2))
pi_half = (np.pi/2) * mag_ones

# MAG_IMG2 WITH PHASE_IMG1
ifft2_img2_img1 = ifft2(mag_fft_img2, phase_fft_img)
plot_img(ifft2_img2_img1.real,'MAGNITUD Img2 PHASE Img1', 'plot1',0,0)

# MAG_IMG1 WITH PHASE_IMG2

ifft2_img1_img2 = ifft2(mag_fft_img, phase_fft_img2)
plot_img(ifft2_img1_img2.real,'MAGNITUD Img1 PHASE Img2', 'plot2', 0, 0)

# MAG_ONES WITH PHASE_IMG1

ifft2_ones_img1 = ifft2(mag_ones, phase_fft_img)
plot_img(ifft2_ones_img1.real,'MAGNITUD ones PHASE Img1', 'plot3', 0, 0.01)

# MAG_ONES WITH PHASE_IMG2

ifft2_ones_img2 = ifft2(mag_ones, phase_fft_img2)
plot_img(ifft2_ones_img2.real,'MAGNITUD Ones PHASE Img2', 'plot4', 0, 0.005)

# MAG_IMG2 WITH PHASE_PIHALF

ifft2_img2_pi = ifft2(mag_fft_img2, pi_half)
plot_img(abs(ifft2_img2_pi), 'MAGNITUD Img2 PHASE Pi/2', 'plot5', 0, 255)

# MAG_IMG1 WITH PHASE_PIHALF

ifft2_img1_pi = ifft2(mag_fft_img, pi_half)
plot_img(abs(ifft2_img1_pi),'MAGNITUD Img1 PHASE Pi/2', 'plot6', 0, 255)