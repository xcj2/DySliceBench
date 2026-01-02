# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)

class weightRtree:
    def __init__(self, num):
        self.num = num
        self.weight = [0] * (num+1) 
      
    def add(self, v, w):
        if v == 0:
            return 0
        while v <= self.num:
            self.weight[v] += w
            v += (-v) & v    

    def getSum(self, u):
        temp = 0
        while u > 0:
            temp += self.weight[u]
            u -= (-u) & u
        return temp

N = int(input())
left = [0] * N
right = [0] * N
Tree = [set(map(int, input().split()[1:])) for i in range(N)]

def DFS(count, source):
    count += 1
    left[source] = count
    for item in Tree[source]:
        count = DFS(count, item)
    count += 1
    right[source] = count
    return count

Object = weightRtree(DFS(1, 0))

Q = int(input())
for i in range(Q):
    alist = list(map(int, input().split()))
    if not alist[0]:
        Object.add(left[alist[1]], alist[2])
        Object.add(right[alist[1]], -alist[2])
    else:
        print(Object.getSum(right[alist[1]] - 1))


