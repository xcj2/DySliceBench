class UnionFind:
    def __init__(self, n): 
        self.par = [-1]*n
        
    def __repr__(self):
        return "union_find({0})".format(self.par)
        
    def unite(self, x, y):
        if self.root(x) != self.root(y):
            self.par[self.root(x)] = y
        
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
        return self.par[x]
        
    def same(self, x, y):
        return self.root(x) == self.root(y)
        
        
from sys import stdin
def readLine_int_list():return list(map(int, stdin.readline().split()))
from collections import defaultdict

def main():
    n,k,l = readLine_int_list()
    
    rail = UnionFind(n)
    road = UnionFind(n)
    
    for _ in range(k):
        p, q = readLine_int_list()
        p, q = p-1, q-1
        road.unite(p, q)
     
    for _ in range(l):
        p, q = readLine_int_list()
        p, q = p-1, q-1
        rail.unite(p, q)
        
    d = defaultdict(int)
    
    for i in range(n):
        d[road.root(i), rail.root(i)] += 1
    results = (d[road.root(i), rail.root(i)] for i in range(n))


    print(" ".join(str(n) for n in results))
    

if __name__ == "__main__":main()