def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil,pi,factorial
    from operator import itemgetter
    def I(): return int(input())
    def MI(): return map(int, input().split())
    def LI(): return list(map(int, input().split()))
    def LI2(): return [int(input()) for i in range(n)]
    def MXI(): return [[LI()]for i in range(n)]
    def SI(): return input().rstrip()
    def printns(x): print('\n'.join(x))
    def printni(x): print('\n'.join(list(map(str,x))))
    inf = 10**17
    mod = 10**9 + 7
#main code here!
#https://note.nkmk.me/python-union-find/

    class UnionFind():
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n
    
        def find(self, x):
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]
    
        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)
    
            if x == y:
                return
    
            if self.parents[x] > self.parents[y]:
                x, y = y, x
    
            self.parents[x] += self.parents[y]
            self.parents[y] = x
    
        def size(self, x):
            return -self.parents[self.find(x)]
    
        def same(self, x, y):
            return self.find(x) == self.find(y)
    
        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]
    
        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]
    
        def group_count(self):
            return len(self.roots())
    
        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}
    
        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    n=I()
    lisx=[]
    lisy=[]
    edge=[]
    for i in range(n):
        x,y=MI()
        lisx.append([x,i])
        lisy.append([y,i])
    lisx.sort(key=lambda x:x[0])
    lisy.sort(key=lambda x:x[0])
    for i in range(n-1):
        edge.append([lisx[i][1],lisx[i+1][1],lisx[i+1][0]-lisx[i][0]])
        edge.append([lisy[i][1],lisy[i+1][1],lisy[i+1][0]-lisy[i][0]])
    edge.sort(key=lambda x:x[2])
    #print(edge)
    ans=0
    uf=UnionFind(n)
    for x,y,z in edge:
        if uf.same(x,y):
            continue
        else:
            uf.union(x,y)
            ans+=z
    print(ans)
        
        
    
if __name__=="__main__":
    main()
