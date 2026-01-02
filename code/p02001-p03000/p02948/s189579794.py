class MaxHeap:
    def __init__(self):
        self.__pq = []
        self.__length = 0
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
N,M = map(int,input().split())
PQ = MaxHeap()
dic = defaultdict(list)
for i in range(N):
    a,b = map(int,input().split())
    dic[a].append(b)
keys = list(dic.keys())
keys.sort()
n = 1
ans = 0
i = 0
ln = len(keys)
while n <= M:
    if i < ln and keys[i] == n:
        for l in dic[keys[i]]:
            PQ.push(l)
        i  += 1
    if not PQ.isempty():
        ans += PQ.popMax()
    n += 1
print(ans)