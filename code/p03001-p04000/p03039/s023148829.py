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
    a, b = LI()
    if a <= 5:
        print(0)
    elif 6 <= a <= 12:
        print(b // 2)
    else:
        print(b)
    return

#B
def B():
    r, d, x = LI()
    for i in range(10):
        print(x * r - d)
        x = x * r - d
    return

#C
def C():
    n, m = LI()
    imo = [0 for i in range(n+1)]
    for _ in range(m):
        l, r = LI_()
        imo[l] += 1
        imo[r + 1] -= 1
    for i in range(1,n):
        imo[i] += imo[i - 1]
    ans = 0
    #print(imo)
    for i in imo:
        if i == m:
            ans += 1
    print(ans)
    return

#D
def D():
    n, m = LI()
    a = LI()
    bc = LIR(m)
    bc.sort(key=lambda x: x[1], reverse=True)
    a.sort()
    index = 0
    suma = 0
    for b, c in bc:
        if index + b >= n:
            if a[n - 1] <= c:
                suma += (n - index) * c
            else: 
                br = bisect_left(a, c)
                if br > index:
                    suma += (br - index) * c
                    index = br
                    break
                else:
                    break
            index = n
            break
        if a[index + b - 1] < c:
            suma += b * c
            index += b
        else:
            if a[index] < c:
                bl = bisect_left(a, c)
                suma += (bl - index) * c
                index = bl
            else:
                break
    suma += sum(a[index:])
    print(suma)

    return

#E
def E():
    n, m, k = LI()
    def cmb(n, r, mod):
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod

    g1 = [1, 1] 
    g2 = [1, 1]
    inverse = [0, 1] 

    for i in range( 2, n*m + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append((g2[-1] * inverse[-1]) % mod)
        
    ans = 0
    for d in range(1,n+1):
        ans += d*cmb(n * m - 2, k - 2, mod) * (n - d) * m ** 2 
    for d in range(1,m+1):
        ans += d*cmb(n * m - 2, k - 2, mod) * (m - d) * n ** 2
    print(ans%mod)
    

    
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    E()
