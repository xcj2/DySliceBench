def examC():
    N = I()
    S = [I() for _ in range(N)]
    S1 = []
    for s in S:
        if s%10==0:
            continue
        S1.append(s)
    if S1==[]:
        print(0)
        return
    S1.sort()
    ans = sum(S)
    if ans%10==0:
        ans -= S1[0]
    print(ans)
    return

def examD():
    N, A, B = LI()
    H = [I() for _ in range(N)]
    H.sort()
    l = 0; r = (H[-1]-1)//B + 1
    while(r-l>1):
        now = (l+r)//2
        cur = 0
        for i in H:
            if i-now*B>0:
                cur += ((i-now*B-1)//(A-B) +1)
        if cur>now:
            l = now
        else:
            r = now
    ans = r
    print(ans)
    return

def examE():
    # 0許容(i += 1)
    class Bit():
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)
            return

        def sum(self, i):
            i += 1
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x=1):
            i += 1
            # i==0 はだめ => 全部+1するとか
            while i <= self.size:
                self.tree[i] += x
                i += i & -i
            return

        def search(self, x):
            # 二分探索。和がx以上となる最小のインデックス(>= 1)を返す
            # maspyさんの参考　よくわかってない
            i = 0
            s = 0
            step = 1 << ((self.size).bit_length() - 1)
            while step:
                if i + step <= self.size and s + self.tree[i + step] < x:
                    i += step
                    s += self.tree[i]
                step >>= 1
            return i

        def debug(self, k):
            return [self.sum(i) for i in range(k)]

        def inversion(self, A=[3, 10, 1, 8, 5]):
            res = 0
            for i, p in enumerate(A):
                self.add(p)
                res += i + 1 - self.sum(p)
            return res
    N, K = LI()
    A = [I()-K for _ in range(N)]
    S = [[0,i] for i in range(N+1)]
    for i in range(N):
        S[i+1][0] = S[i][0]+A[i]
    S.sort()
    prev = -inf
    cnt = -1
    for i in range(N+1):
        if S[i][0]==prev:
            S[i][0] = cnt
        else:
            prev = S[i][0]
            cnt += 1
            S[i][0] = cnt
    S.sort(key=lambda x:x[1])
    A = [0]*(1+N)
    for i in range(N+1):
        A[i] = S[i][0]
    bit = Bit(cnt+1)
    #print(A)
    ans = N*(N+1)//2 - bit.inversion(A)
    if ans<0:
        ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examE()

"""

"""