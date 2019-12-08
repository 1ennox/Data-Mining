from numpy import *


def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split()
        fltLine = list(map(eval, curLine))
        dataMat.append(fltLine)
    return dataMat


# Euclidean distance between 2 vectors
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


# random generate centroids
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = float(max(array(dataSet)[:, j]) - minJ)
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids


def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))  # create mat to assign data points
    # to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):  # for each data point assign it to the closest centroid
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI;
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist ** 2
        print(centroids)
        for cent in range(k):  # recalculate centroids
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]  # get all the point in this cluster
            centroids[cent, :] = mean(ptsInClust, axis=0)  # assign centroid to mean
    return centroids, clusterAssment


def show(dataSet, k, centroids, clusterAssment):
    from matplotlib import pyplot as plt
    numSamples, dim = dataSet.shape
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    for i in range(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=12)
    plt.xlabel("MinTemp")
    plt.ylabel("MaxTemp")
    plt.show()


dataMat = mat(loadDataSet('test.txt'))
myCentroids, clustAssing = kMeans(dataMat, 4)
print(myCentroids)
show(dataMat, 4, myCentroids, clustAssing)
