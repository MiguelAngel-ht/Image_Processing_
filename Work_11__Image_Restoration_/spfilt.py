"""
----------------------------------------------------------------------------------------

matlab code from:
https://github.com/taivop/eth-ml/blob/master/p3/feature_engineering/DIPUMToolboxV1.1.3/spfilt.m

SPFILT Performs linear and nonlinear spatial filtering.
F = SPFILT(G, TYPE, M, N, PARAMETER) performs spatial filtering
of image G using a TYPE filter of size M-by-N. Valid calls to
SPFILT are as follows: 

    #      F = SPFILT(G, 'amean', M, N)       Arithmetic mean filtering.
    #      F = SPFILT(G, 'gmean', M, N)       Geometric mean filtering.
    #      F = SPFILT(G, 'hmean', M, N)       Harmonic mean filtering.
    #      F = SPFILT(G, 'chmean', M, N, Q)   Contraharmonic mean
    #                                         filtering of order Q. The
    #                                         default is Q = 1.5.
    #      F = SPFILT(G, 'median', M, N)      Median filtering.
    #      F = SPFILT(G, 'max', M, N)         Max filtering.
    #      F = SPFILT(G, 'min', M, N)         Min filtering.
    #      F = SPFILT(G, 'midpoint', M, N)    Midpoint filtering.
    #      F = SPFILT(G, 'atrimmed', M, N, D) Alpha-trimmed mean filtering.
    #                                         Parameter D must be a
    #                                         nonnegative even integer;
    #                                         its default value is D = 2.

-------------------------------------------------------------------------------------

        Python Version by Miguel Ángel Hernánez Tapia :)

"""

# Main libraries
from cv2 import filter2D, medianBlur
from cv2 import BORDER_REPLICATE, BORDER_REFLECT
import numpy as np

# Auxiliar libraries
from ordfilt2 import *
from symmetric_padding import *

global eps
eps = 0.000001   # most be very small

def spfilt(img, typ, m=3, n=3, parameter=0):
    
    if parameter == 0:
        Q = 1.5
        d = 2 
    else:
        Q = d = parameter
    
    # SWITCH CASE OF EVERY MODE

    if typ == 'amean':
        kernel = (1 / (m*n)) * np.ones((m,n))
        f = filter2D(img, -1, kernel, BORDER_REPLICATE)
    elif typ == 'gmean':
        f = gmean(img, m, n)
    elif typ == 'hmean':
        f = harmean(img, m, n)
    elif typ == 'chmean':
        f = charmean(img, m, n, Q)
    elif typ == 'median':
        f = medianBlur(img, m)
    elif typ == 'max':
        f = ordfilt2(img, m*n-1, np.ones((m, n)))
    elif typ == 'min':
        f = ordfilt2(img, 0, np.ones((m, n)))
    elif typ == 'midpoint':
        f1 = ordfilt2(img, 0, np.ones((m, n)))
        f2 = ordfilt2(img, m*n-1, np.ones((m, n)))
        f = 0.5*f1 - 0.5*f2
    elif typ == 'atrimmed':
        if d <= 0 or d/2 != d//2:
            print('d must be a positive, even integer.')
            return 0
        f = alphatrim(img, m, n, d)
    else:
        f = medianBlur(img, m)

    f = f.astype('int')
    return f

def gmean(img, m, n):
    # Implements a geometric mean filter.
    try:
        f = np.exp(filter2D(np.log(img), -1, np.ones((m, n)), BORDER_REPLICATE))
        f = f  ** (1 / m / n)
    except:
        f = img
    return f

def harmean(img, m, n):
    #  Implements a harmonic mean filter.
    
    f = m * n / filter2D(1 / (img + eps), -1, np.ones((m, n)), BORDER_REPLICATE)

    return f

def charmean(img, m, n, q):
    #  Implements a contraharmonic mean filter.
    img = img.astype('float')
    f = filter2D(np.power(img,q+1), -1, np.ones((m, n)), BORDER_REPLICATE)
    f = f / (filter2D( np.power(img, q), -1, np.ones((m, n)), BORDER_REPLICATE) + eps)
    
    return f

def alphatrim(img, m, n, d):
    #  Implements an alpha-trimmed mean filter.

    f = filter2D(img, -1, np.ones((m, n)), BORDER_REFLECT)

    for k in range( d//2 ):
        f = f - ordfilt2(img, k, np.ones((m, n)))

    for k in np.arange((m*n - (d//2) + 1), m*n, 1):
        f = f - ordfilt2(img, k, np.ones((m, n)))

    f = f // (m*n - d)

    return f



# One pixel bordering

def symmetric_border(img):

    # dimentions of new image 
    m, n = np.shape(img)
    im = np.zeros((m+2, n+2))

    # convention of limits
    M = m+1; N = n+1           # limits of new image
    m = m-1; n = n-1           # limits of original image

    # centering image
    im[1:M,1:N] = img

    # reflect
    im[1:M, 0] = img[0:m+1, 0]
    im[1:M, N] = img[0:m+1, n]
    im[0, 1:N] = img[0, 0:n+1]
    im[M, 1:N] = img[m, 0:n+1]

    # corners
    im[0,0] = img[0,0]
    im[0,N] = img[0,n]
    im[M,0] = img[m,0]
    im[M,N] = img[m,n]
    
    return 
    





