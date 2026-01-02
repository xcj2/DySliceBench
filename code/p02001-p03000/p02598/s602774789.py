def examA():
    X = I()
    if X<30:
        ans = "No"
    else:
        ans = "Yes"
    print(ans)
    return

def examB():
    N, D = LI()
    cnt = 0
    for _ in range(N):
        x, y = LI()
        if x**2+y**2<=D**2:
            cnt += 1
    ans = cnt
    print(ans)
    return

def examC():
    N = 10**7
    K = I()
    cur = 0
    now = 1
    ans = -1
    for i in range(N):
        cur += 7 * now
        cur %= K
        if cur==0:
            ans = i+1
            break
        now *= 10
        now %= K
    print(ans)
    return

def examD():
    N = I()
    C = SI()
    cnt = 0
    l = 0; r = N-1
    while(l<r):
        while(l<N):
            if C[l]=="W":
                break
            l += 1
        while(0<=r):
            if C[r]=="R":
                break
            r -= 1
        if l<r:
            cnt += 1
            l += 1
            r -= 1
    ans = cnt
    print(ans)
    return

def examE():
    N, K = LI()
    A = LI()
    if K==0:
        print(max(A))
        return
    l = 0; r = inf
    while(r-l>1):
        now = (l+r)//2
        cnt = 0
        for a in A:
            cur = a//now
            if a%now==0:
                cur -= 1
            cnt += cur
        if cnt<=K:
            r = now
        else:
            l = now
        #print(now,cnt)
        #input()
    ans = r

    print(ans)
    return

def examF():
    # 0は絶対に入れない!!
    class Bit():
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)
            return

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x=1):
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
            return i + 1

        def debug(self, k):
            return [self.sum(i) for i in range(k)]

        def inversion(self, A=[3, 10, 1, 8, 5]):
            res = 0
            for i, p in enumerate(A):
                self.add(p, 1)
                res += i + 1 - self.sum(p)
            return res
    N, Q = LI()
    C = LI()
    LR = []
    lastAppeared = [-1]*N
    for i in range(Q):
        l, r = LI()
        LR.append((l,r,i))
    LR.sort(key=lambda x:x[1])
    #print(LR)
    bit = Bit(N+1)
    ans = [0]*Q
    r = 0
    now = 0
    while(r<N):
        if now==Q:
            break
        l0, r0, i0 = LR[now]
        while(r<r0):
            c = C[r]-1
            if lastAppeared[c]>0:
                bit.add(lastAppeared[c],-1)
            lastAppeared[c] = r+1
            bit.add(lastAppeared[c]+1)
            r += 1
        #print(bit.debug(r))

        while(now<Q):
            l0,r0,i0 = LR[now]
            if r<r0:
                break
            #print(r,now)
            ans[i0] = bit.sum(r0)
            if l0>1:
                ans[i0] -= bit.sum(l0-1)
            now += 1


    for v in ans:
        print(v)
    return

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep,alphabet_convert
mod = 10**9 + 7
mod2 = 998244353
inf = 1<<60
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 9

sys.setrecursionlimit(10**5)

if __name__ == '__main__':
    examE()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""