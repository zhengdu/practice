#! /Users/zheng/anaconda/bin/python

import numpy as np
import operator
import matplotlib.pyplot as plt
import ipdb
import math 
from collections import Counter  

decisionNode = dict(boxstyle = "sawtooth",fc="0.8")
leafNode = dict(boxstyle = "round4",fc="0.8")
arrow_args = dict(arrowstyle = "<-")

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
	createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords="axes fraction", xytext=centerPt, textcoords='axes fraction',
		                    va='center', ha='center', bbox=nodeType, arrowprops=arrow_args)

def createPlot():
	fig = plt.figure(1, facecolor = 'white')
	fig.clf()
	ipdb.set_trace()
	createPlot.ax1 = plt.subplot(111,frameon = False)
	ipdb.set_trace()
	plotNode('a decision node', (0.5,0.1), (0.1,0.5), decisionNode)
	plotNode('a leaf node', (0.8,0.1), (0.3,0.8), leafNode)
	plt.show()


createPlot()		