# -*- coding: utf-8 -*-
'''
所要時間は、分位であった。
'''
# ライブラリのインポート
#import re #正規表現
import sys
#import heapq
import bisect
#import collections
#import math

def main():
    n = int(input())
    X = [[] for i in range(n)]
    l = []
    for i, line in enumerate(sys.stdin):
        X[i] = list(line.strip("\n").split())
        for j in range(i,n):
            c = int(X[i][j])
            if c == -1:
                continue
            else:
                r = (c,i,j)
                bisect.insort(l, r)
    
    uf = UnionFind(n)
    k = 0
    ans = 0
    count = 0
    while(count < n):
        try: tmp = l[k]
        except: break
        x = tmp[1]
        y = tmp[2]
        if not uf.same(x,y):
            uf.unite(x, y)
            ans += tmp[0] 
            count += 0
        k += 1
    print(ans)

class UnionFind:
    def __init__(self,n):
        self.p = [i for i in range(n)]
        return
    
    def root(self,x):
        while(1):
            if (self.p[x] == x): break
            y = x
            x = self.p[x]
            self.p[y] = self.p[x]
        return x

    def unite(self ,x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return
        else:
            self.p[rx] = ry
            return 
    
    def same(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry


    
if __name__ == '__main__':
    main()

