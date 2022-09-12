#!/usr/bin/python3
import math


class Quicker:
    size = 0
    arr = []

    def __init__(self,A):
        self.arr = A
        self.size = len(A)
    
    def fix(self,head,tail):
        if(tail-head>=2):         
            middle = math.floor((head+tail)/2)
            tailValue = self.getNode(tail)
            headValue = self.getNode(head)
            middleValue = self.getNode(middle)
            #比较中间值
            if( (headValue>tailValue and headValue<middleValue) or (headValue>middleValue and headValue<tailValue) ):
                self.exchange(head,tail)
            elif( (middleValue>tailValue and middleValue<headValue) or (middleValue>headValue and middleValue<tailValue) ):
                self.exchange(middleValue,tail)

    def quickSort(self,p,r):
        if p<r:
            q = self.partition(p,r)
            self.quickSort(p,q-1)
            self.quickSort(q+1,r)

    def partition(self,p,r):
        self.fix(p,r)
        x = self.getNode(r)
        i = p-1
        for j in range(p,r):
            if( self.getNode(j)<x ):
                i=i+1
                self.exchange(i,j)
                     
        self.exchange(i+1,r)
        return i+1

    def sort(self):
        self.quickSort(1,self.size)
    
    def exchange(self,node1,node2):
        temp = self.getNode(node1)
        self.setNode(node1,self.getNode(node2))
        self.setNode(node2,temp)

    def setNode(self,node,node2):
        self.arr[node-1] = self.arr[node2-1]

    def setNode(self,node,value):
        self.arr[node-1] = value

    def getNode(self,node):
        return self.arr[node-1]

    def getA(self):
        return self.arr


myArr = []
for i in range(0,10):
    myArr.append( int( input("please input a number:") ) )
sorter = Quicker(myArr)
print(sorter.getA())
sorter.sort()
print("after insertion sort process")
print(sorter.getA())
