import numpy as np

"""
    The function receives an image and returns 3 times larger 
    with the image in the middle and on the sides a reflection (mirror).
    
    * Image must be cuadratic  M x M

    i =  Original image.
    a =  Horizontal mirror. 
    b =  Vertical mirror.
    c =  Transpose of original image.
    d =  Transpose of secondary diagonal of original image.

    Result:

          d  a  c
    pad = b  i  b
          c  a  d

    By Miguel Ángel Hernández Tapia :)

"""

def symmetric_padding(img): 

    a = np.flipud(img)          # horizonatal mirror
    b = np.fliplr(img)          # vertical mirror
    c = img.T                   # Transpose \
    d = np.matrix(img)
    d[0:,0:] = d[0:,0:][::-1].transpose()[::-1]      # Transpose of secondary diagonal /

    # The matrices are concatenated horizontally
    pad1 = np.append(d, a, axis=1)
    pad1 = np.append(pad1, c, axis=1)

    pad2 = np.append(b, img, axis=1)
    pad2 = np.append(pad2, b, axis=1)
    
    pad3 = np.append(c, a, axis=1)
    pad3 = np.append(pad3, d, axis=1)    

    #               pad 1
    #       pad  =  pad 2
    #               pad 3

    pad = np.append(pad1, pad2, axis=0)
    pad = np.append(pad, pad3, axis=0)

    return np.array(pad)  # convert to numpy array

