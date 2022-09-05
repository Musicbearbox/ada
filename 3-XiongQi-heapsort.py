#!/usr/bin/python3
import math


class MHeap:
    heapSize = 0
    heap = []

    def __init__(self,A):
        self.heap = A
        self.heapSize = len(A)
    
    def buildMaxHeap(self):
        startNode = self.parent(self.heapSize)
        for i in range(startNode,0,-1):
            self.maxHeapify(i)
        # print(self.heap)

    def maxHeapify(self,i):
        l = self.left(i)
        r = self.right(i)
        if l<=self.heapSize and self.getNode(l) > self.getNode(i):
            largest = l
        else :
            largest = i
        if r<= self.heapSize and self.getNode(r) > self.getNode(largest):
            largest = r
        if largest != i:
            self.exchange(i,largest)
            self.maxHeapify(largest)

    def heapSort(self):
        self.buildMaxHeap()
        for i in range (self.heapSize,1,-1):
            self.exchange(1,i)
            # print(self.heap)
            self.heapSize = self.heapSize-1
            self.maxHeapify(1)
    
    def exchange(self,node1,node2):
        temp = self.getNode(node1)
        self.setNode(node1,self.getNode(node2))
        self.setNode(node2,temp)

    def setNode(self,node,node2):
        self.heap[node-1] = self.heap[node2-1]
    
    def left(self,node):
        return node*2
    
    def right(self,node):
        return (node*2)+1

    def parent(self,node):
        return math.floor(node/2)

    def setNode(self,node,value):
        self.heap[node-1] = value

    def getNode(self,node):
        return self.heap[node-1]

    def getA(self):
        return self.heap


myArr = []
for i in range(0,10):
    myArr.append( int( input("please input a number:") ) )
heap1 = MHeap(myArr)
print(heap1.getA())
heap1.heapSort()
print("after insertion sort process")
print(heap1.getA())
