"""
---------------------------------------------------------------------------------------
matlab code from
https://github.com/omartrinidad/preprocessing/blob/master/adpmedian.m

ADPMEDIAN Perform adaptive median filtering.
   F = ADPMEDIAN(G, SMAX) performs adaptive median filtering of
   image G.  The median filter starts at size 3-by-3 and iterates up
   to size SMAX-by-SMAX. SMAX must be an odd integer greater than 1.

   Copyright 2002-2004 R. C. Gonzalez, R. E. Woods, & S. L. Eddins
   Digital Image Processing Using MATLAB, Prentice-Hall, 2004
   $Revision: 1.5 $  $Date: 2003/11/21 14:19:05 $

SMAX must be an odd, positive integer greater than 1.
--------------------------------------------------------------------------------------

 Python Version by Miguel Ángel Hernánez Tapia :)

"""

import numpy as np
from spfilt import ordfilt2


def adpmedian(img, smax, mode=''):
      
    if smax <= 1 or smax/2 == np.round(smax/2) or smax != np.round(smax):
        print('SMAX must be an odd integer > 1.')
        return 0
    M, N = np.shape(img)

    # where filtered image will saved
    f = np.zeros((M,N))

    # Boolean matrix with False in every position
    alreadyProcessed = np.ones((M,N)) 
    alreadyProcessed = f > alreadyProcessed

    # Begin filtering.
    if mode == 'quick':
        iter = [smax]
    else:
        iter = np.arange(3, smax+1, 2)

    for k in iter:
        zmin = ordfilt2(img, 0, np.ones((k, k)))
        zmax = ordfilt2(img, k*k-1, np.ones((k, k)))
        zmed = ordfilt2(img, (k*k-1)//2, np.ones((k, k)))
       
        processUsingLevelB = (zmed > zmin) & (zmax > zmed) & (~ alreadyProcessed)
        zB = (img > zmin) & (zmax > img)
        outputZxy  = processUsingLevelB & zB
        outputZmed = processUsingLevelB & (~ zB)
        f[outputZxy] = img[outputZxy]
        f[outputZmed] = zmed[outputZmed]
        
        alreadyProcessed = alreadyProcessed | processUsingLevelB
        if alreadyProcessed.all():
            break

    
    f[~ alreadyProcessed] = zmed[~ alreadyProcessed]
    return f
