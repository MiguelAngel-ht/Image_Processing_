# **Equalization Step by Step vs OpenCV Function**

In this code, we compare the final equalizated image vs the result of function from OpenCV. 
The main idea is obtain normalized histogram and cumulative histograma from normal image and then, obtain equalization transform and also its histograms. 
Finally repeat the process since equalization transform and compare histograms and images.


**Histogram** is a graphical representation of the distribution of data. 

**Normalized Histogram** is a histogram but values from 0 to 1 and the sum of all values is 1.

**Cumulative Histogram** is a histogram where every values is cumulated.

**Normalized Cumulative Histogram** is similar to cumulative histogram but values from 0 to 1 and the last value is equal to 1.
