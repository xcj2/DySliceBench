#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a, p = LI()
    print((a*3+p)//2)
    return

#B
def B():
    n = II()
    sp = []
    for i in range(n):
        sp.append(input().split())
    another = [(s[0], -1 * int(s[1]),num) for num,s in enumerate(sp)]
    another.sort()
    for s,p,q in another:
        print(q+1)

    return

#C
def C():
    n, m = LI()
    ks = LIR_(m)
    p = LI()
    patern = itertools.product(range(2), repeat=n)
    ans = 0
    for on in patern:
        ki = [0 for i in range(m)]
        for num, oni in enumerate(on):
            if oni:
                for i,ksi in enumerate(ks):
                    ksi = ksi[1::]
                    if num in ksi:
                        ki[i] ^= 1
        for num, pi in enumerate(p):
            if pi != ki[num]:
                break
        else:
            ans += 1
    print(ans)

            
    return

#D
def D():
    N, K = LI()#random.randint(1,50),random.randint(1,100)
    v = LI()#[random.randint(-10 ** 2, 10 ** 2) for i in range(N)]
    ans = 0
    for a in range(min(N, K) + 1):
        for b in range(min(N, K) + 1):
            if a + b > min(K,N):
                break
            if a == b == 0:
                continue
            deletes = K - a - b
            left = v[:a]
            right = v[:-b-1:-1]
            x = left + right
            x.sort()
            tmp = sum(x)
            for delete in range(min(deletes, len(x))):
                if x[delete] >= 0:
                    break
                tmp -= x[delete]
            ans = max(ans,tmp)
    
    print(ans)
                

    return


#E
def E():  
    N,q = LI()
    STX = LIR(N)
    D = IR(q)
    LV = (q - 1).bit_length()
    N0 = 1 << LV

    data = [inf] * (N0 << 1)
    INF = inf

    def update(l, r, x):
    
        #  区間[l, r)のdataの値を更新
        L = N0 + l; R = N0 + r
        while L < R:
            if R & 1:
                R -= 1
                data[R-1] = min(data[R-1], x)
            if L & 1:
                data[L-1] = min(data[L-1], x)
                L += 1
            L >>= 1; R >>= 1

    def query(x):
        L = N0 + x - 1
        #  xの最小値を求める
        s = INF
        while L >= 0:
            s = min(s, data[L])
            L = (L - 1) >> 1
        return s

    for s, t, x in STX:
        XS = max(-1, s - x)
        XT = max(-1, t - x)
        XS_index = bisect_left(D, XS)
        XT_index = bisect_left(D, XT)
        update(XS_index, XT_index, x)

    for i in range(q):
        a = query(i)
        print(a if a != inf else -1)
#F
def F():
    return

#Solve
if __name__ == '__main__':
    E()
