# -*- coding: utf-8 -*-
"""TAREA 5 | Ecualización e Histogramas_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cp0dCE7axDTO7Bt3wyeDDrm2KMX__f1n

# **Equalization Step by Step vs OpenCV Function**

In this code, we compare the final equalizated image vs the result of function from OpenCV. The main idea is obtain normalized histogram and cumulative histograma from normal image and then, obtain equalization transform and also its histograms. Finally repeat the process since equalization transform and compare histograms and images.
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

"""# **PART 1: Step by Step Equalization**"""

img = cv.imread('/content/azathoth.PNG',0)    # 0 -> grayscale 

plt.title('Imagen Original')
plt.imshow(img,'gray')
plt.show()

np.shape(img)

"""**Histogram** is a graphical representation of the distribution of data. 

**Normalized Histogram** is a histogram but values from 0 to 1 and the sum of all values is 1.

**Cumulative Histogram** is a histogram where every values is cumulated.

**Normalized Cumulative Histogram** is similar to cumulative histogram but values from 0 to 1 and the last value is equal to 1.
"""

def histograms(img):
  # IMAGE HISTOGRAM
  hist, bins = np.histogram(img.flatten(), 256, [0, 256])
  # normalized histogram
  hist_norm = hist / hist.max()
  # cumulative histogram
  hist_cum = hist.cumsum()
  # normalized cumulative histogram
  hist_cum_norm = hist_cum / hist_cum.max()
  return hist_norm, hist_cum_norm

# Function recieve histogram and title to plot respective histogram

def hisplot(hist, title):
  # CREATE FIGURE
  plt.figure(figsize=(10,3))
  plt.title(title)
  plt.xlabel("Intensidad")
  plt.ylabel("Número de Pixeles")
  # STEM PLOT
  markerline, stemlines, baseline = plt.stem(
    hist, linefmt ='orange', markerfmt =' ',
    bottom = 0, use_line_collection = True)
  markerline.set_markerfacecolor('none')
  baseline.set_color('k')

  plt.xlim([0, 256])
  plt.show()

hist_norm, hist_cum_norm = histograms(img)
hisplot(hist_norm, 'Histograma Normalizado')

hisplot(hist_cum_norm, 'Histograma Acumulado Normalizado')

cdf_m = np.ma.masked_equal(hist_cum_norm, 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img_equal = cdf[img]

plt.title('Equalizado Paso a Paso')
plt.imshow(img_equal,'gray')
plt.show()

hist_norm_eq, hist_cum_norm_eq = histograms(img_equal)

hisplot(hist_norm_eq, 'Histograma Normalizado Img. Ecualizada')

hisplot(hist_cum_norm_eq, 'Histograma Acum. Normalizado Img. Ecualizada')

"""# **PART 2: OpenCV Fuction**"""

# EQUALIZATION
equ = cv.equalizeHist(img)

# HISTOGRAMS
hist_norm_eq, hist_cum_norm_eq = histograms(equ)

plt.title('Equalizado con OpenCV')
plt.imshow(equ,'gray')
plt.show()

hisplot(hist_norm_eq, 'Histograma Normalizado Img. Ecualizada OpenCV')

hisplot(hist_cum_norm_eq, 'Histograma Acum. Normalizado Img. Ecualizada OpenCV')