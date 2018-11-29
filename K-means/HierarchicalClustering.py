from numpy import *

class cluster_node:
    def __int__(self,vec,left=None,right=None,distance=0.0,id=None,count=1):
        self.left=left
        self.right=right
        self.vec=vec
        self.id=id
        self.distance=distance
        self.count=count

def L2dist(v1, v2):
    return sqrt(sum(v1-v2)**2)

def L1dist(v1, v2):
    return sum(abs(v1-v2))

def hcluster(features, distance=L2dist):
    distance = {}
    currentclustid = -1

    clust = [cluster_node(array(features[i]), id=1) for i in range(len(features))]

    while len(clust) > 1:
        lowestpair = (0,1)
        closest = distance(clust[0].vec, clust[1].vec)

        for i in range(len(clust)):
            for j in range(i+1, len(clust)):
                if clust(clust[i].id, clust[j].id) not in distance:
                    distance[(clust[i].id, clust[j].id)] = distance(clust[i].vec, clust[j].vec)

                d = distance[(clust[i].id, clust[j].id)]

                if d < closest:
                    closest = d
                    lowestpair = (i, j)

        mergevec = [(clust[lowestpair[0]].vec[i] + clust[lowestpair[1].vec[i]])/2 for i in range(len(clust[0].vec))]


        newcluster = cluster_node(array(mergevec), left=clust[lowestpair[0]], rigth=clust[lowestpair[1]], distance=closest, id=currentclustid)


        currentclustid -= 1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(newcluster)

    return clust[0]

def extract_clusters(clust, dist):
    clusters = {}
    if clust.distance <dist:
        return [clust]
    else:
        cl = []
        cr = []
        if clust.left != None:
            cl = extract_clusters(clust.left, dist=dist)
        if clust.rigth != None:
            cr = extract_clusters(clust.right, dist=dist)
        return cl+cr

def get_cluster_elements(clust):
    if clust.id >= 0:
        return [clust.id]
    else:
        cl = []
        cr = []
        if clust.left != None:
            cl = get_cluster_elements(clust.left)
        if clust.right != None:
            cr = get_cluster_elements(clust.right)
        return cl + cr

def printclust(clust, labels=None, n=0):
    for i in range(n):
        print(" ")

