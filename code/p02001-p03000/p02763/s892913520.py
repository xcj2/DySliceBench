import sys
from collections import defaultdict, deque, Counter
import math
 
# import copy
from bisect import bisect_left, bisect_right
# import heapq
 
# sys.setrecursionlimit(1000000)
 
# input aliases
input = sys.stdin.readline
 
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]
 
INF = 10 ** 20
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

class Segtree_op():
     # 単位元及び操作を設定して使うこと
     # queryでは、区間の(l, r)を指定する ex: (0, 5) => [0, 1, 2, 3, 4]
     # 特定の1点は (i, i+1)
     def __init__(self, n):
         self.size = 1
         while(n >= 1):
             self.size = self.size << 1
             n = n//2
 
         self.arr = [self.unit() for i in range(self.size*2)]
 
     def op(self, lch, rch):
         # update min with holding index
         return max(rch, lch)
     def unit(self):
         return 0
 
     def update(self, k, val):
         k += self.size - 1
         self.arr[k] = val
         while(k):
             k = (k - 1) // 2
             self.arr[k] = self.op(self.arr[k*2 + 1], self.arr[k*2 + 2])
 
     def query(self, l, r):
         L = l + self.size
         R = r + self.size
         s = self.unit()
         while L < R:
             if R & 1:
                 R -= 1
                 s = self.op(s, self.arr[R - 1])
 
             if L & 1:
                 s = self.op(s, self.arr[L - 1])
                 L += 1
             L >>= 1
             R >>= 1
         return s
 
 
     def show(self):
         idx = 1
         while(idx <= self.size):
             print(self.arr[idx - 1:idx * 2 - 1])
             idx *= 2
 

def getind(c):
    return ord(c) - ord("a")

def main():
    N = getN()
    S = list(getS())
    Q = getN()
    segs = [Segtree_op(N) for i in range(26)]
    for i, c in enumerate(S):
        segs[getind(c)].update(i, 1)

    for _ in range(Q):
        query = getS().split()
        if query[0] == "1":
            k, i, c = query
            i = int(i) - 1
            segs[getind(S[i])].update(i, 0)
            segs[getind(c)].update(i, 1)
            S[i] = c
        else:
            k, l, r = list(map(int, query))
            ans = 0
            for se in segs:
                if se.query(l-1, r) == 1:
                    ans += 1

            print(ans)


if __name__ == "__main__":
    main()
   