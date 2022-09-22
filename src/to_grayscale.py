#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    pass

def to_red(image):
    pass

def to_green(image):
    pass

def to_blue(image):
    pass



def main():
    image = plt.imread("src/painting.png")
    result = to_grayscale(image)
    plt.imshow(result, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    fig, ax = plt.subplots(3,1)
    
    #Uncomment after finishing part 1
    #ax[0].imshow(to_red(image))
    #ax[1].imshow(to_green(image))
    #ax[2].imshow(to_blue(image))
    #plt.show()

if __name__ == "__main__":
    main()
