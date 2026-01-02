# coding: utf-8

def getBList(A):
    bList = []
    for i in range(1, len(A)+1):
        bList.append(A[i-1]-i)
    return bList

def getMedian(bList):
    tmp = sorted(bList)
    if len(bList) % 2 == 1:
        return tmp[len(bList)//2]
    else:
        return (tmp[len(bList)//2]+tmp[len(bList)//2-1])//2

def solve(A, b):
    ssum = 0
    for i in range(len(A)):
        ssum += abs(A[i] - (b+i+1))
    return ssum

if __name__ == "__main__":

    N = int(input())
    A = [int(x) for x in input().split()]
    print(solve(A, getMedian(getBList(A))))
 
