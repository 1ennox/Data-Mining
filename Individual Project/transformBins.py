import cv2
import matplotlib.pyplot as plt
import numpy as np


def to_bin(lena2):  # only when bin number is 2 will this function be used
    arr_lena = np.asarray(lena2)  # transform the picture into array type, otherwise, errors will occur
    for row in range(len(arr_lena)):
        for column in range(len(arr_lena[row])):  # for each pixel of the graph
            if (arr_lena[row][column] >= 255 / 2).any():  # if this pixel's value is less than 127.5, make it white
                arr_lena[row][column] = 255
            else:  # otherwise, make it black
                arr_lena[row][column] = 0
    plt.subplot(2, 3, 1)
    plt.title("2 Bins")
    plt.imshow(arr_lena)


def to_x_bins(lena, bins):
    if (bins == 2):
        to_bin(lena)
        return;
    arr_lena = np.asarray(lena)
    for row in range(len(arr_lena)):
        for column in range(len(arr_lena[row])):
            for x in range(1, bins):  # bins = how many bins that are going to be generated
                split = 255 * (1 / bins) / 2  # spilt = half of a bin
                if (arr_lena[row][column] < split).any():  # the first bin
                    arr_lena[row][column] = 0
                elif (arr_lena[row][column] >= 255 * (x / bins) - split).any():
                    if (arr_lena[row][column] < 255 * (x / bins) + split).any():  # if this pixel is in this bin
                        arr_lena[row][column] = 255 * (x / bins)  # change it's value, otherwise, try the next bin
                elif (arr_lena[row][column] >= 255 - split).any():  # the last bin
                    arr_lena[row][column] = 255
    plt.subplot(2, 3, bins - 1)
    plt.imshow(arr_lena)
    plt.title("%s Bins" % bins)


for bin in range(2, 8):
    print(bin)
    lena2 = cv2.imread('lena.png')
    lena2 = cv2.cvtColor(lena2, cv2.COLOR_BGR2RGB)
    #    to_bin(lena2)
    to_x_bins(lena2, bin)
plt.show()
