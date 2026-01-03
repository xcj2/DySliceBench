#import numpy as np
#from numpy import*
#from scipy.sparse.csgraph import shortest_path #shortest_path(csgraph=graph)
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse.csgraph import floyd_warshall
#from scipy.sparse import csr_matrix

#from collections import* #defaultdict Counter deque appendleft
#from fractions import gcd
#from functools import* #reduce
#from itertools import* #permutations("AB",repeat=2) combinations("AB",2) product("AB",2) groupby accumulate
#from operator import mul,itemgetter
#from bisect import* #bisect_left bisect_right
#from heapq import* #heapify heappop heappushpop
#from math import factorial,pi
#from copy import deepcopy
import sys
#sys.setrecursionlimit(10**8)
input=sys.stdin.readline  #危険！基本オフにしろ！

class UNION_FIND(object):
    def __init__(self,n):
        self.parent=[-1 for i in range(n)]
        
    def root(self,x):
        if self.parent[x]<0:
            return x
        else:
            self.parent[x]=self.root(self.parent[x])
            return self.parent[x]
 
    def size(self,x):
        return -self.parent[self.root(x)]
    def union(self,x,y):
        x=self.root(x)
        y=self.root(y)
        if x==y:
            return False
        if self.size(x)<self.size(y):
            x,y=y,x
        self.parent[x]+=self.parent[y]
        self.parent[y]=x
        return True

def compute_mst_kruskal(max_v, edges, flip):
    edges.sort(key=lambda x: x[2],reverse=flip)
    uf = UNION_FIND(max_v)
    mst = []
    for (a,b,c) in edges:
        if uf.root(a)!= uf.root(b):
            uf.union(a,b)
            mst.append(c)
    return mst


def main():
    n=int(input())
    inp=[[i]+list(map(int,input().split()))for i in range(n)]
    inpX=sorted(inp,key=lambda x:x[1])
    inpY=sorted(inp,key=lambda x:x[2])
    edges=[]
    for i in range(1,n):
        a,b,c=inpX[i]
        d,e,f=inpX[i-1]
        edges.append((a,d,min(abs(b-e),abs(c-f))))
        a,b,c=inpY[i]
        d,e,f=inpY[i-1]
        edges.append((a,d,min(abs(b-e),abs(c-f))))
    
    print(sum(compute_mst_kruskal(n, edges, 0)))
        
    
if __name__ == '__main__':
    main()