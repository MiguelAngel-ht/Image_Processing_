import numpy as np
from symmetric_padding import *

"""
--------------------------------------------------------------------------------------
    This function receives the image to be convoluted, 
    the order to be taken and the domain that will be discarded.

    For example:
    order = 4
    domain  =  [[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]

    kernel =  [[1,8,3],
               [7,5,6],
               [9,2,1]]
    
    kernel = domain * kernel

    kernel.sort() = [1,1,2,3,5,6,7,8,9] 
                    -0-1-2-3-4-5-6-7-8-   positions
    
    kernel[order=3] = 4

    if order == 0 will be taken the minimum
    if order == 8 will be taken the maximum

    If domain have 0 values in some positions, this values were discarted
    * Works better with images without 0 values
----------------------------------------------------------------------------------------
    
    Autor: Miguel Ángel Hernández Tapia :)

"""

def ordfilt2(img, order, domain): # 3x3 kernel
    
    # adding border 
    im = symmetric_padding(img)
    M, N = np.shape(img)

    # variable where result will be saved
    img_fil = np.zeros((M,N))
    
    # select necessary borders to convolution 3->1  5->3  7->5
    k = len(domain)
    bor = k-2
    im =  im[M-bor:2*M+bor, N-bor:2*N+bor]

    # CONVOLUTION
     
    if domain.all():     # Condition to avoid overcalculations
        for i in range(M):
            for j in range(N):
                kernel = im[i:i+k, j:j+k]
                kernel = np.sort(kernel, axis=None)  # sort a list with every value
                img_fil[i,j] = kernel[order]         # take the value for position "order" 0-minimum and 8-maximum
    else:
        for i in range(M):
            for j in range(N):
                kernel = domain * im[i:i+k, j:j+k]   # domain 1 to pass or 0 to null 
                kernel = np.sort(kernel, axis=None)  # sort a list with every value
                kernel = np.delete(kernel, np.where(kernel == 0))  # discat 0 values
                img_fil[i,j] = kernel[order]         # take the value for position "order" 0-minimum and 8-maximum
    
    return img_fil             
