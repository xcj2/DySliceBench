def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    class minseg():
        
        def __init__(self, arr):
            self.n = len(arr)
            self.ide_ele = arr[0]
            self.num =2**((self.n-1).bit_length())
            self.seg=[self.ide_ele]*2*self.num
            for i in range(self.n):
                self.seg[i+self.num-1]=arr[i]
            for i in range(self.num-2,-1,-1) :
                self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 

        def segfunc(self, x, y):
            return min(x, y)

            
        def update(self, k, x):
            k += self.num-1
            self.seg[k] = x
            while k:
                k = (k-1)//2
                self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])
            
        def query(self, p, q):
            if q<=p:
                return self.ide_ele
            p += self.num-1
            q += self.num-2
            res=self.ide_ele
            while q-p>1:
                if p&1 == 0:
                    res = self.segfunc(res,self.seg[p])
                if q&1 == 1:
                    res = self.segfunc(res,self.seg[q])
                    q -= 1
                p = p//2
                q = (q-1)//2
            if p == q:
                res = self.segfunc(res,self.seg[p])
            else:
                res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
            return res

    class maxseg():
        
        def __init__(self, arr):
            self.n = len(arr)
            self.ide_ele = arr[0]
            self.num =2**((self.n-1).bit_length())
            self.seg=[self.ide_ele]*2*self.num
            for i in range(self.n):
                self.seg[i+self.num-1]=arr[i]
            for i in range(self.num-2,-1,-1) :
                self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 

        def segfunc(self, x, y):
            return max(x, y)

            
        def update(self, k, x):
            k += self.num-1
            self.seg[k] = x
            while k:
                k = (k-1)//2
                self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])
            
        def query(self, p, q):
            if q<=p:
                return self.ide_ele
            p += self.num-1
            q += self.num-2
            res=self.ide_ele
            while q-p>1:
                if p&1 == 0:
                    res = self.segfunc(res,self.seg[p])
                if q&1 == 1:
                    res = self.segfunc(res,self.seg[q])
                    q -= 1
                p = p//2
                q = (q-1)//2
            if p == q:
                res = self.segfunc(res,self.seg[p])
            else:
                res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
            return res

    n = int(input())
    a = list(map(int, input().split()))

    ind = {}
    for i in range(n):
        ind[a[i]] = i
    smax = maxseg([0]*(n+1))
    smin = minseg([n+1]*(n+1))

    res = 0
    for i in range(n):
        # 配列の1-indexed
        pos = ind[n-i] + 1

        l1 = smax.query(0, pos)
        l2 = smax.query(0, l1)
        r1 = smin.query(pos, n+2)
        r2 = smin.query(r1+1, n+2)
        res += ((l1-l2)*(r1-pos) + (r2-r1)*(pos-l1)) * (n-i)

        smin.update(pos, pos)
        smax.update(pos, pos)

    print(res)

if __name__ == '__main__':
    main()