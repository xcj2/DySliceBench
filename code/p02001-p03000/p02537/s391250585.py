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
    class SegmentTree:#非再帰(こちらの方が速い) #1-indexed
        # 初期化処理
        # f : SegmentTreeにのせるモノイド
        # default : fに対する単位元
        def __init__(self, size, f=lambda x,y : max(x,y), default=0):
            self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
            self.default = default
            self.dat = [default]*(self.size*2) # 要素を単位元で初期化
            self.f = f
    
        def update(self, i, x):
            i += self.size
            self.dat[i] = x
            while i > 0:
                i >>= 1
                self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])
    
        def query(self, l, r):
            l += self.size
            r += self.size
            lres, rres = self.default, self.default
            while l < r:
                if l & 1:
                    lres = self.f(lres, self.dat[l])
                    l += 1
    
                if r & 1:
                    r -= 1
                    rres = self.f(self.dat[r], rres) # モノイドでは可換律は保証されていないので演算の方向に注意
                l >>= 1
                r >>= 1
            res = self.f(lres, rres)
            return res
    n,k=MI()
    seg=SegmentTree(size=2*300000+1)
    for i in range(n):
        x=I()
        mx=seg.query(300000+x-k,300000+x+k+1)
        #print(mx,x)
        seg.update(300000+x,mx+1)
    print(seg.query(0,2*300000+2))
        
    
    
    
    








if __name__=="__main__":
    main()

