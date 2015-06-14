#! /Users/zheng/anaconda/bin/python

import numpy as np
import operator
import matplotlib.pyplot as plt
import pdb
import math 
from collections import Counter  

def calcShannonEnt(data):
	dataSet = np.array(data)
	numEntries = len(dataSet)
	tag = dataSet[:,-1]
	counts = Counter(tag)
	entropy = 0
	for key in counts:
		prob = float(counts[key])/numEntries
		entropy -= prob * math.log(prob, 2)

	return entropy 	

def createDataSet():
	dataSet = [[1,1,'yes'],
		       [1,1,'yes'],
		       [1,0,'no'],
		       [0,1,'no'],
		       [0,1,'no']]
	labels = ['no surfacing','flippers']
	return dataSet, labels

def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for sample in dataSet:
		if sample[axis] == value:
			reducedFeat = sample[:axis]
			reducedFeat.extend(sample[axis+1:])
			retDataSet.append(reducedFeat)
			
	return retDataSet	    


def chooseBestFeatureToSplit(dataSet):
	numFeature = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0
	bestFeature = -1

	for i in range(numFeature):
		featList = [example[i] for example in dataSet ]
		uniqueVal = set(featList)
		newEntropy = 0.0
		for value in uniqueVal:
			subDataSet = splitDataSet(dataSet,i,value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy +=  prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i

	return bestFeature			

def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys(): classCount[vote] = 0
		classCount[vote] += 1

	sortedClassCount = sorted(classCount.itms(),key=operator.itemgetter(1),reverse = True)
	return sortedClassCount[0][0]

def createTree(dataSet,labels):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel:{}}
	del (labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVal = set(featValues)
	for value in uniqueVal:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)

	return myTree
