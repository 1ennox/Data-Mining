import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import pandas as pd
from sklearn import preprocessing
from scipy.stats import norm
from scipy import stats

stream1D = np.random.randint(0, 100, size = [1000, 1])
stream2D = np.random.randint(0, 100, size = [1000, 2])
stream3D = np.random.randint(0, 100, size = [1000, 3])

# generate a 1D scatterpoint graph
plot.scatter(stream1D, np.zeros_like(stream1D) + 0)
plot.title("1D scatterpoint graph")
plot.show()
# generate a 2D scatterpoint graph
plot.scatter(stream2D[:,0],stream2D[:,1])
plot.title("2D scatterpoint graph")
plot.show()

# generate a 3D scatterpoint graph
fig = plot.figure()
ax = Axes3D(fig)
ax.scatter(stream3D[:, 0], stream3D[:, 1], stream3D[:, 2])
ax.set_zlabel('Z')  # axis
ax.set_ylabel('Y')
ax.set_xlabel('X')
plot.title("3D scatterpoint graph")
plot.show()

# histogram and pdf of 1D data
sns.distplot(stream1D[:,0], color='g')
plot.title("histogram and pdf of 1D data")
plot.show()
# histogram and pdf of 2D data
sns.distplot(stream2D[:,0], color='g')
sns.distplot(stream2D[:,1], color='b')
plot.title("histogram and pdf of 2D data")
plot.show()
# histogram and pdf of 3D data
sns.distplot(stream3D[:,0], color='r')
sns.distplot(stream3D[:,1], color='g')
sns.distplot(stream3D[:,2], color='b')
plot.title("histogram and pdf of 3D data")
plot.show()
