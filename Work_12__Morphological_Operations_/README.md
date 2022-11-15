# Morphological Operations

They are those that change the image by importing the shape of the image itself and the kernel.

### Erosion

The basic idea of erosion is how soil erosion only, erodes the boundaries of the foreground object (always try to keep the foreground blank).

### Dilate

It is just the opposite of erosion. Therefore, it increases the white region in the image or increases the size of the foreground object.

### Opening

The opening is just another name for erosion followed by dilation. It is useful for eliminating noise.

### Closing

Closure is the reverse of opening, dilation followed by erosion. It is useful for closing small holes within foreground objects, or small black dots in the object.

![Exa](https://bioimagebook.github.io/_images/morph_4_0.png)


<p align="center" width="60%">
    <img width="60%%" src="https://bioimagebook.github.io/_images/morph_4_0.png">
</p>

## Acknowledgements
*Documentation of specific functions was inserted just click on it :) 
 - [Python](https://www.python.org/)
 - [Numpy](https://numpy.org/doc/stable/reference/generated/numpy.ones.html)
 - [Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html)
 - [Plotly](https://plotly.com/python/imshow/)
 - [OpenCV](https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html)

## Authors

- [Miguel Ángel Hernández Tapia](https://github.com/MiguelAngel-ht)

