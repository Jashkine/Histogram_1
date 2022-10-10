# Histogram computation

import numpy as np                      #Import Numpy
import skimage
from skimage import io, color
import matplotlib.pyplot as plt


def histogram_computation(img2):        #Funtion definition
    '''Histogram computation
        the function takes image as input
        returns 1D array of size 256 containing intensity frequency'''
    arr2 = [0]*256                      #Create 1D array of 256 size
    img1 = np.array(img2,int)           #Convert input image to a 2D numpy array
    for _ in img1:                      #Sweep through each pixel of image
        for i in _:
            arr2[i] = arr2[i]+1         #Computing frequency of intensities present in image
    return arr2

if __name__ =='__main__':
    x = np.array(range(0, 256))                                     #define values in x axis
    image = skimage.io.imread('./Images/Lena_original_gray.png')    #Reading Image
    imgGray = (color.rgb2gray(image))*255                           #converting image to gray
    histo = histogram_computation(imgGray)                          #Calling histogram function
    plt.figure(1)                                                   #plotting the image and histogram
    plt.suptitle("Histogram", fontsize=15)
    plt.subplot(121)
    plt.imshow(image, cmap="gray", vmin=0, vmax=255)
    plt.title("Original Image")
    plt.subplot(122)
    plt.bar(x,histo, width=1)
    plt.title("Histogram of an Image")
    plt.show()
