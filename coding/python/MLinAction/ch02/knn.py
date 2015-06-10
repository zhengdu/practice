#! /Users/zheng/anaconda/bin/python

import numpy as np
import operator
import matplotlib.pyplot as plt
import pdb

def createDataSet():
	group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = np.array(['A','A','B','B'])
	return group, labels


def classify0(inX,dataSet,labels,k):
	dist = np.sum(np.power((dataSet - inX), 2),1)
	ind = dist.argsort()[0:k]
	ll = labels[ind]
	vote = {}
	for label in ll:
		if label in vote:
			vote[label] += 1
		else:
			vote[label] = 1
	sortedVote = sorted(vote.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVote[0][0]		

def file2matrix(filename):
	data = np.loadtxt(filename,delimiter='\t')
	mat = data[:,0:3]
	label = data[:,3]
	return mat, label

def autoNorm(dataSet):
	minVal = dataSet.min(0)
	maxVal = dataSet.max(0)
	ranges = maxVal - minVal
	normDataSet = (dataSet - minVal)/ranges
	return 	normDataSet, ranges, minVal

def datingClassTest():
	hoRatio = 0.10
	datingDataMat,datingLabels = file2matrix('/Users/zheng/Code/MLinAction/Ch02/datingTestSet2.txt')
	normMat, ranges, minVal = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVects = int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVects):
		classiferResult = classify0(normMat[i,:],normMat[numTestVects:m,:],datingLabels[numTestVects:m],3)
		if (classiferResult != datingLabels[i]): errorCount += 1

	print 'The total error rate is: %f' %(errorCount/float(numTestVects))	 	