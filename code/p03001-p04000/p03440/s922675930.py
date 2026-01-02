import sys
from heapq import heapify, heappop, heappush

class UFT(): #Union-find tree class
    def __init__(self, N): 
        self.tree = [int(i) for i in range(N)] 
        self.rank = [0 for i in range(N)]

    def find(self, a):
        if self.tree[a] == a: return a
        else:
            self.tree[a] = self.find(self.tree[a])
            return self.tree[a]

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
        if self.rank[a] < self.rank[b]: self.tree[a] = b
        else:
            self.tree[b] = a
            if self.rank[a] == self.rank[b]: self.rank[a] += 1
def solve():
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]
    parent = UFT(N)
    for i in range(M):
        x, y = map(int, input().split())
        parent.unite(x, y)
    totalForest = 0
    minCost = 0
    minF = dict()
    for i in range(N):
        a = parent.find(i)
        if a in minF: heappush(minF[a], A[i])
        else: 
            minF[a] = []
            heapify(minF[a])
            heappush(minF[a], A[i])
            totalForest += 1

    f = []
    heapify(f)
    sonNode = []
    heapify(sonNode) 
    if totalForest > 1:
        for key in minF: 
            minCost += heappop(minF[key])
            while minF[key]: heappush(sonNode, heappop(minF[key]))
   
    for _ in range(max(totalForest - 2, 0)):
        if not sonNode: 
            print("Impossible")
            break
        minCost += heappop(sonNode)
    else: print(minCost)
    return 0

if __name__ == "__main__":
    solve()