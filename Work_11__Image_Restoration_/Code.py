# BASIC LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# FUNCTIONS FROM .py FILES
from ImScale import * 
from histplot import *
from spfilt import *
from adpmedian import *

# READ IMAGE
img = cv.imread('FigP0501(noisy_superconductor_image).tif', 0)
cv.imwrite('Original_superconductor.png', img)
# plt.imshow(img, 'gray')
# plt.show()

# Select Region of Interest
x, y, w, h = 38, 197, 44, 73 

# Interactive selection of region of interest
# x, y, w, h = cv.selectROI(img)
# print(x,y,w,h)

# ROI of Image 
roi = img[y:y+h, x:x+w]

# ROI without Image
roipoly = np.zeros(np.shape(img))
roipoly[y:y+h, x:x+w] = 255
cv.imwrite('ROI_polygon.png', roipoly)
# plt.imshow(roipoly, 'gray')
# plt.show()

# ROI in image
im_roi = roipoly
im_roi[y:y+h, x:x+w] = roi
cv.imwrite('ROI_in_image.png', im_roi)
# plt.imshow(im_roi, 'gray')
# plt.show()

# Histogram of ROI
roi
hist_roi, bins = np.histogram(roi.flatten(), 256, [0, 256])
histplot(hist_roi, 'roi_hist', 'ROI Histogram')


# Simulation noise to compare with roi
M, N = np.shape(roi)
k = -1 / 15  # -1/a
# Exponential Noise
Ruido_Exp =  k*np.log(1 - np.random.rand(M,N))
Ruido_Exp = ImScale(Ruido_Exp).astype('int')

# Histogram of Exponential 
hist, bins = np.histogram(Ruido_Exp.flatten(), 256, [0, 256])
histplot(hist, 'exp_hist', 'Exponential Histogram')


# READ salt noise image
img_salt = cv.imread('FigP0502(a)(salt_only).tif', 0)
cv.imwrite('salt_noise.png', img_salt)
# plt.imshow(img_salt, 'gray')
# plt.show()

# CONTRA HARMONIC MEAN FILTERING
img_salt_fil = spfilt(img_salt, 'chmean', 3, 3, -2)
cv.imwrite('salt_noise_filtered.png', img_salt_fil)
# plt.imshow(img_salt_fil, 'gray')
# plt.show()

# READ pepper noise image

img_pepper = cv.imread('FigP0502(b)(pepper_only).tif', 0)
cv.imwrite('pepper_noise.png', img_pepper)
# plt.imshow(img_pepper, 'gray')
# plt.show()

# CONTRA HARMONIC MEAN FILTERING
img_pepper_fil = spfilt(img_pepper, 'chmean', 3, 3, 1)
cv.imwrite('pepper_noise_filtered.png', img_pepper_fil)
# plt.imshow(img_pepper_fil, 'gray')
# plt.show()


# ADAPTATIVE MEDIAN FILTERING with kernels 3x3 5x5 7x7 and 9x9

img_salt_fil_adp = adpmedian(img_salt, 9)
cv.imwrite('salt_noise_filt_adapt.png', img_salt_fil_adp)
# plt.imshow(img_salt_fil_adp, 'gray')
# plt.show()

img_pepper_fil_adp = adpmedian(img_pepper, 9)
cv.imwrite('pepper_noise_filt_adapt.png', img_pepper_fil_adp)
# plt.imshow(img_pepper_fil_adp, 'gray')
# plt.show()