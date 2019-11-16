import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2

lena = cv2.imread('lena.png') # import the lena picture
lena_gray = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY) # transform it into greyscale
plt.imshow(lena_gray, cmap='gray')
plt.show()


def get_row_view(a):  # to get mode of the picture
    void_dt = np.dtype((np.void, a.dtype.itemsize * np.prod(a.shape[-1])))
    a = np.ascontiguousarray(a)
    return a.reshape(-1, a.shape[-1]).view(void_dt).ravel()


def get_mode(lena_gray):  # to get mode of the picture
    unq, idx, count = np.unique(get_row_view(lena_gray), return_index=1, return_counts=1)
    return lena_gray.reshape(-1,lena_gray.shape[-1])[idx[count.argmax()]]

mean = np.mean(lena_gray)
std = np.std(lena_gray)
median = np.median(lena_gray)
min = np.min(lena_gray)
max = np.max(lena_gray)
count = np.bincount(get_mode(lena_gray))
mode = np.argmax(count)
print("The mean value of the picture is: ", mean)
print("The standard deviation of the picture is: ", std)
print("The median value of the picture is: ", median)
print("The min value of the picture is: ", min)
print("The max deviation value of the picture is: ", max)
print("The mode value of the picture is: ", mode)

plt.hist(lena_gray.ravel(),256,[0,256]);
plt.title("Histogram of lena_gray")
plt.show()

# print the 3D shape of the picture (using intensity as the third dimension)
xx, yy = np.mgrid[0:lena_gray.shape[0], 0:lena_gray.shape[1]]
fig = plt.figure(figsize=(15,15))
ax = fig.gca(projection='3d')
ax.plot_surface(xx, yy, lena_gray ,rstride=1, cstride=1, cmap=plt.cm.gray,linewidth=2)
ax.view_init(80, 30)
plt.title("3D shape with the intensity as the third dimension")
plt.show()