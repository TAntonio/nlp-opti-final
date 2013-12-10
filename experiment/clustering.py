#!/usr/bin/python
#
# clustering.py
#
# clusters bags-of-words according to their feature vectors

from __future__ import division
import sys, os, subprocess, math

def main():
    #develop arrays of dates and feature vectors
    featurestrings=open("../data/featurevectors","r+").readlines()
    dates=[]
    vecs=[]
    for feat in featurestrings:
        dates.append(feat.split()[0])
        tovec=feat[12:]
        intstrings=tovec.split(",")
        vector=[]
        for item in intstrings:
            item=item.strip()
            if item.endswith("]"):
                item=item.rstrip("]")
            vector.append(item)
        vecs.append(vector)

    #initial distance
    distance=1000000
    
    #indices of vectors of initial centers
    centers=[vecs[113], vecs[114], vecs[115], vecs[116]]

    #which cluster is each vector in?

    while not distance == 0:
        clusters=[]
        clustermeans=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        clustersizes=[0,0,0,0]
        #initialize the distance for these clusters
        distance2=0

        #which cluster are we in?
        for vec in vecs:
            cl=0
            smallestdist=1000000
            for cen in centers:
                dist=0
                for i in range(len(vec)):
                    a=int(vec[i]) - int(cen[i])
                    a**=2
                    dist+=a
                dist=math.sqrt(dist)
                if dist < smallestdist:
                    cl=centers.index(cen)
                    smallestdist=dist
            clusters.append(cl)
            clustersizes[cl]+=1
            distance2+=smallestdist

        #calculate the mean distance for every cluster
        for vec in vecs:
            for index in vec:
            #for vec's cluster
                clustermeans[clusters[vecs.index(vec)]][vec.index(index)]+=int(index)
        #print clustersizes
        for i in range(len(clustermeans)):
            for j in range(len(clustermeans[i])):
                clustermeans[i][j]/=clustersizes[i]
                #print clustermeans[i][j]
                
        #print clustermeans
        for cl in clustermeans:
            centers[clustermeans.index(cl)]=cl
            #print cl    

        #if we get the same distance two times in a row...
        if distance2==distance:
            break
        else:
            distance=distance2


    #determining clusters--which one is which?
    #sums in order: happy, content, sad, angry, clusters 0 1 2 3
    sums=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(clusters)):
        sums[clusters[i]][0]=sums[clusters[i]][0]+int(vecs[i][0])+int(vecs[i][1])+int(vecs[i][2])+int(vecs[i][3])+int(vecs[i][4])+int(vecs[i][17])+int(vecs[i][18])+int(vecs[i][20])
        sums[clusters[i]][1]=sums[clusters[i]][1]+int(vecs[i][5])+int(vecs[i][6])+int(vecs[i][7])+int(vecs[i][8])+int(vecs[i][9])+int(vecs[i][18])
        sums[clusters[i]][2]=sums[clusters[i]][2]+int(vecs[i][10])+int(vecs[i][11])+int(vecs[i][12])+int(vecs[i][13])+int(vecs[i][14])+int(vecs[i][19])
        sums[clusters[i]][3]=sums[clusters[i]][3]+int(vecs[i][15])+int(vecs[i][16])+int(vecs[i][17])+int(vecs[i][19])+int(vecs[i][20])+int(vecs[i][21])
        
    for i in range(len(sums)):
        for j in range(len(sums[i])):
            sums[i][j]/=clustersizes[i]
        
    clusterfeels=["","","",""]
    happy=-1
    content=-1
    sad=-1
    angry=-1
    unclassifiedcl=[0,1,2,3]
    unclassifiedfl=[0,1,2,3]
    while len(unclassifiedcl) > 0:
        for j in unclassifiedcl:
            greatest=-1
            val=-1
            bestj=-1
            for i in unclassifiedfl:
                if sums[j][i] > greatest:
                    greatest = sums[j][i]
                    val=i
                    bestj=j
            if val == 0:
                clusterfeels[bestj]="happy"
                
            if val == 1:
                clusterfeels[bestj]="content"
                
            if val == 2:
                clusterfeels[bestj]="sad"
                
            if val == 3:
                clusterfeels[bestj]="angry"
        unclassifiedfl.remove(val)
        unclassifiedcl.remove(bestj)
            
    

    for i in range(len(dates)):
        #print clusters[i]
        print dates[i]+": today I felt "+clusterfeels[clusters[i]]+"."

if __name__=="__main__":
    main()
