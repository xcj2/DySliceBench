class MaxHeap:
    def __init__(self):
        self.__pq = []
        self.__length = 0

    def __str__(self):
        return self.__pq.__str__()
    
    def length(self):
        return self.__length
    
    def push(self,item):
        self.__pq.append(item)
        self.__length += 1
        i = self.__length - 1
        while i > 0:
            p = (i-1)//2
            tmp = self.__pq[p]
            if tmp >= item:
                break
            self.__pq[p] = item
            self.__pq[i] = tmp
            i = p
    
    def popMax(self):
        if self.__length == 0:
            return None
        ret = self.__pq[0]
        if self.__length == 1:
            self.__length -= 1
            return self.__pq.pop(0)
        self.__pq[0] = self.__pq.pop(self.__length-1)
        self.__length -= 1
        i = 0
        while 2*i+1 < self.__length:
            larger = 2*i+1
            if 2*i+2 < self.__length:
                if self.__pq[2*i+2] > self.__pq[larger]:
                    larger = 2*i+2
            tmp = self.__pq[larger]
            if tmp <= self.__pq[i]:
                break
            self.__pq[larger] = self.__pq[i]
            self.__pq[i] = tmp
            i = larger
        return ret
    
    def isempty(self):
        return self.__length == 0
from collections import defaultdict
X,Y,Z,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

PQ = MaxHeap()
used = defaultdict(bool)
PQ.push((A[0]+B[0]+C[0],0,0,0))
cnt = 0
arr = []
while cnt < K:
    s,i,j,k = PQ.popMax()
    if not used[(i,j,k)]:
        arr.append(s)
        used[(i,j,k)] = True
        if i+1 < X and not used[(i+1,j,k)]:
            PQ.push((A[i+1]+B[j]+C[k], i+1,j,k))
        if j+1 < Y and not used[(i,j+1,k)]:
            PQ.push((A[i]+B[j+1]+C[k], i,j+1,k))
        if k+1 < Z and not used[(i,j,k+1)]:
            PQ.push((A[i]+B[j]+C[k+1], i,j,k+1))
        cnt += 1
for i in range(K):
    print(arr[i])