#!/usr/bin/python3

import math

# count = 0

def MaxCrossingSubarray(A,low,mid,high):
    left_sum = A[mid]
    max_left = mid
    sum = 0
    for i in range(mid,low-1,-1):
        sum = sum + A[i]
        if left_sum<sum:
            left_sum = sum
            max_left = i
    # print(low)
    # print(mid)
    # print(high)
    # print(left_sum)

    right_sum = A[mid+1]
    max_right = mid+1
    sum = 0
    for i in range(mid+1,high+1):
        sum = sum + A[i]
        if right_sum < sum:
            right_sum = sum
            max_right = i

    return (max_left,max_right,left_sum+right_sum)


def findMaximumSubarray( A,low,high ):
    mid = math.floor((low+high)/2)
    # global count
    # count= count+1
    # print(count)
    if low == high:
        return (low,high,A[high])
    elif (low+1) == high:
        (left_low,left_high,left_sum) = findMaximumSubarray(A,low,mid)
        (right_low,right_high,right_sum) = findMaximumSubarray(A,mid+1,high)
        (cross_low,cross_high,cross_sum) = MaxCrossingSubarray(A,low,mid,high)
    else:
        
        (left_low,left_high,left_sum) = findMaximumSubarray(A,low,mid)
        (right_low,right_high,right_sum) = findMaximumSubarray(A,mid,high)
        (cross_low,cross_high,cross_sum) = MaxCrossingSubarray(A,low,mid,high)

    if left_sum>=right_sum and left_sum>= cross_sum:
        return (left_low,left_high,left_sum)
    elif right_high>=left_high and right_sum>cross_sum:
        return (right_low,right_high,right_sum)
    else:
        return (cross_low,cross_high,cross_sum)


myArr = []
for i in range(0,6):
    myArr.append( int( input("please input a change number:") ) )
print(myArr)
(low,height,sum) = findMaximumSubarray(myArr,0,len(myArr)-1)
print("after process")
print(low,height,sum)
