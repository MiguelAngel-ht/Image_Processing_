# -*- coding: utf-8 -*-
"""Tarea 12 | Operaciones Morfológicas .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1soQ1EzmRFF_R85oOhPvvKy2TJJsly8AF
"""

# Importing libreries 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# To measure seconds o execution
from datetime import datetime

"""## Functions"""

# Function to scale a image from min to max

def ImScale(img, minf=0, maxf=255):

    x_min = img.min()
    x_max = img.max()

    return minf + ((img - x_min) / (x_max - x_min)) * (maxf - minf)

# Add constant border of 0 en a matrix 
def constant_border(img):
  N, M = np.shape(img)
  img_out = np.zeros((N+2,M+2), np.uint8)
  img_out[1:N+1,1:M+1] = img
  return img_out

# Simulation of function of Matlab 
def bwlabel(img):

  img_out = img
  x = 0
  y = 0
  label = 1
  N, M = np.shape(img_out)

  for i in range(N):
    for j in range(M):
      if img_out[i][j] == 255:
        
        for k in np.arange(j, M, 1):  #---->
          if img_out[i, k] == 255: 
            x += 1
          else:
            break                                    
                                      # |
        for k in np.arange(i, N, 1):  # v 
          if img_out[k, j] == 255:
            y += 1
          else:
            break

        img_out[i:i+y,j:j+x] = label
        label += 1
        x = 0 
        y = 0
        
  return img_out

# Reducted version of first function
def bwlabel2(img):

  img.astype('uint8')
  label = 1
  N, M = np.shape(img)

  for i in range(N):
    for j in range(M):

      if img[i][j] == 255:

        x = np.argmin(img[i,j:j+150])                            
        y = np.argmin(img[i:i+150,j])

        img[i:i+y,j:j+x] = label
        label += 1
        
  return img

# Obtaining vertices and center of rectangles
def bwhitmiss(img):

  vertices, centers = [], []
  N, M = np.shape(img)

  for i in range(10):
    for j in range(M):
      if img[i][j] != 0:
 
        x = np.argmin(img[i,j:])                            
        y = np.argmin(img[i:,j])
        print(img[i:i+y,j:j+x])
        img[i:i+y,j:j+x] = 0
        img[i,j] =  255
        img[i,j+x-1] =  255
        img[i+y-1,j] =  255
        img[i+y-1,j+x-1] = 255
        print(img[i:i+y,j:j+x])
        vertices.append([(i,j), (i,j+x), (i+y,j), (i+y,j+x)])
        centers.append((i + y//2, j + x//2))
        
  return img, vertices, centers

"""# Code

## **Characters Counting**
"""

img = cv.imread('Fig1022(a).tif', 0)
plt.figure(figsize=(8,12))
plt.imshow(img, 'gray')
plt.show()

kernel = np.ones((3,3))
img_op = cv.dilate(img, kernel)

fig = px.imshow(img_op, color_continuous_scale='gray')
fig.show()

kernel = np.ones((4, 4))
img_op2 = cv.dilate(img, kernel)
img_op[700:,:] = img_op2[700:,:]

fig = px.imshow(img_op, color_continuous_scale='gray')
fig.show()

kernel = np.ones((1,5))
opening = cv.morphologyEx(img_op, cv.MORPH_OPEN, kernel)

fig = px.imshow(opening, color_continuous_scale='gray')
fig.show()

text = """ponents or broken connection paths There is no poition past the level of detail required to identify those Segmentation of nontrivial images is one of the mo processing Segmentation accuracy determines the ev of computerized analysis procedures For this reason be taken to improve the probability of rugged segment such as industrial inspection applications at least some the environment is possible at times The experienced designer invariably pays considerable attention to suc"""
len(text.replace(' ', ''))

img_lab = cv.connectedComponentsWithStats(opening, cv.CV_32S)

img_lab[0]

img_labed = img_lab[1]

n, m = np.shape(img_labed)

for i  in range(img_lab[0]):
  if img_lab[2][i][-1] < 350:
    img_labed[img_labed == i] = 0

for i in range(n):
  label = img_labed[i, m-1]
  if label != 0:
    img_labed[img_labed == label] = 0

img_labed[img_labed != 0] = 255
img_labed = img_labed.astype('uint8')
cv.imwrite('letters_clear.png', img_labed)

output = cv.connectedComponentsWithStats(img_labed, cv.CV_32S)
(num_lab, img_lab, stats, centroids) = output

num_lab

fig = px.imshow(img_lab, color_continuous_scale='gray')
fig.show()

"""## **Rectangle Caracteristics**"""

img2 = cv.imread('Fig1013(a).tif', 0)
plt.figure(figsize=(8,8))
plt.imshow(img2, 'gray')
plt.show()

# start_time = datetime.now()

# img2_label = bwlabel(img2)

# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))

# start_time = datetime.now()

# img2_label = bwlabel2(img2)

# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))

start_time = datetime.now()

(n_lab, img2_label, stats, centroids) = cv.connectedComponentsWithStats(img2,
                                                                        cv.CV_32S)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

img2_label = ImScale(img2_label)
fig = px.imshow(img2_label, color_continuous_scale='gray')
fig.show()

print('Num \t Center \t Area \t    Vertices')
for i in range(n_lab-1):
  print(i,'\t', np.round(centroids[i+1],1),'\t', stats[i+1][-1],'\t',
        stats[i+1][0:2],
        stats[i+1][0:2] + [stats[i+1][2],0],
        stats[i+1][0:2] + [0, stats[i+1][3]],
        stats[i+1][0:2] + [stats[i+1][2], stats[i+1][3]]
        )

"""# Segmentación"""

img3 = cv.imread('Fig1026(a).tif', 0)
plt.imshow(img3, 'gray')
plt.show()

img3_umb_1 = cv.threshold(img3, 135, 245, cv.THRESH_BINARY)[1]
plt.imshow(img3_umb_1, 'gray')
plt.show()

img3_umb_2 = cv.threshold(img3, 110, 240, cv.THRESH_BINARY)[1]
plt.imshow(img3_umb_2, 'gray')
plt.show()

img3_umb_1[350:,:] = img3_umb_2[350:,:] 
plt.imshow(img3_umb_1, 'gray')
plt.show()

kernel = np.ones((3,3),np.uint8)
opening = cv.morphologyEx(img3_umb_1, cv.MORPH_OPEN, kernel)

# SCALING IN 0 AND 255 VALUES
thresh_image = cv.threshold(opening, 0, 255, cv.THRESH_BINARY)[1]
np.unique(thresh_image)

fig = px.imshow(thresh_image, color_continuous_scale='gray')
fig.show()

# apply connected component analysis to the thresholded image
output = cv.connectedComponentsWithStats(thresh_image, cv.CV_32S)
(numLabels, labels, stats, centroids) = output

numLabels

labels = ImScale(labels)
fig = px.imshow(labels, color_continuous_scale='gray')
fig.show()

mask = labels.astype('bool')
intens = mask * img3

intensities = []
mean_intens = np.zeros(np.shape(labels))

# Loop of every label to obtain intensities of original image to measure 
# mean and set in other images
for i in range(numLabels-1):
  locs = np.where(labels == i+1)
  pixels = intens[locs]
  mean = np.mean(pixels)
  intensities.append(mean)
  mean_intens[locs] = mean

fig = px.imshow(intens, color_continuous_scale='gray')
fig.show()

cv.imwrite('celulas_intensidades_medias.png', mean_intens)
fig = px.imshow(mean_intens, color_continuous_scale='gray')
fig.show()

print('Num \t Center \t Area \t Intensidad Media')
for i in range(numLabels-1):
  print(i,'\t', np.round(centroids[i+1],1),'\t',
        stats[i+1][-1],'\t', intensities[i].round(2))

# REFERENCES

# https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
# https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html