import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N = int(input())
    A = [int(x) for x in input().split()]

    indexList = {x : i for i, x in enumerate(A)}

    V = set()
    rootList = {}
    size = {}

    def getRoot(index):
        parent = rootList[index]
        if parent == index:
            return index
        root = getRoot(parent)
        rootList[index] = root
        return root

    def union(x, y):
        rootX, rootY = getRoot(x), getRoot(y)
        sX, sY = size[rootX], size[rootY]
        if sX > sY:
            sX, sY = sY, sX
            rootX, rootY = rootY, rootX
        rootList[rootX] = rootY
        size[rootY] += sX

    ans = 0
    for x in range(N, 0, -1):
        index = indexList[x]
        V.add(index)
        size[index] = 1
        rootList[index] = index
        left, right = 0, 0

        if index - 1 in V:
            left = size[getRoot(index - 1)]
            union(index, index - 1)
        if index + 1 in V:
            right = size[getRoot(index + 1)]
            union(index, index + 1)

        count = (left + 1) * (right + 1)
        ans += x * count

    print(ans)


sol()