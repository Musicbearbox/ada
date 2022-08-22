#!/usr/bin/python3

def insertionSort( arr1 ):
    for j in range(1,len(arr1)):
        key = arr1[j]
        #insertion sort process
        i = j - 1
        while i >=0 and arr1[i]>key:
            arr1[i+1] = arr1[i]
            i = i-1
            
        arr1[i+1]=key


myArr = []
for i in range(0,10):
    myArr.append( int( input("please input a number:") ) )
print(myArr)
insertionSort(myArr)
print("after insertion sort process")
print(myArr)



