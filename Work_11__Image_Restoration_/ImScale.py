# Function to scale a image from min to max

def ImScale(img, minf=0, maxf=255):

    x_min = img.min()
    x_max = img.max()

    return minf + ((img - x_min) / (x_max - x_min)) * (maxf - minf)
    
     