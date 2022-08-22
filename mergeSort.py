import math
from re import L


def mergeSort( A,p,r ):
    if p<r:
        q= math.ceil((p+r)/2)
        mergeSort(A,p,q-1)
        mergeSort(A,q,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    n1 = q-p
    n2 = r-q+1
    mLeft = []
    mRight = []
    for i in range(0,n1):
        mLeft.append(A[p+i])

    for i in range(0,n2):
        mRight.append(A[q+i])
    i = 0
    j = 0
    lenOfLeft = len(mLeft)
    lenofRight = len(mRight)
    for k in range(p,r+1):
        if i >= lenOfLeft and j >= lenofRight:
            break;
        elif i>=lenOfLeft:
            A[k] = mRight[j]
            j = j + 1
        elif j>=lenofRight:
            A[k] = mLeft[i]
            i = i + 1
        elif mLeft[i] <= mRight[j]:
            A[k] = mLeft[i]
            i = i + 1
        else:
            A[k] = mRight[j]
            j = j + 1



myArr = []
for i in range(0,10):
    myArr.append( int( input("please input a number:") ) )
print(myArr)
mergeSort(myArr,0,len(myArr)-1)
print("after merge sort process")
print(myArr)






