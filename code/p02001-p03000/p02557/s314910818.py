def main():
    examF()

def examA():
    N = I()
    ans = 1^N
    print(ans)
    return

def examB():
    a, b, c, d = LI()
    ans = max(a*c,a*d,b*c,b*d)
    print(ans)
    return

def examC():
    N = I()
    if N==1:
        ans = 0
    else:
        ans = pow(10,N,mod) - pow(9,N,mod)*2 + pow(8,N,mod)
        ans += mod*2
        ans %= mod
    print(ans)
    return

def examD():
    class combination():
        # 素数のmod取るときのみ　速い
        def __init__(self, n, mod):
            self.n = n
            self.mod = mod
            self.fac = [1] * (n + 1)
            self.inv = [1] * (n + 1)
            for j in range(1, n + 1):
                self.fac[j] = self.fac[j - 1] * j % mod

            self.inv[n] = pow(self.fac[n], mod - 2, mod)
            for j in range(n - 1, -1, -1):
                self.inv[j] = self.inv[j + 1] * (j + 1) % mod

        def comb(self, n, r):
            if r > n or n < 0 or r < 0:
                return 0
            return self.fac[n] * self.inv[n - r] * self.inv[r] % self.mod
    S = I()
    C = combination(S,mod)
    cnt = 0
    for i in range(S//3):
        cur = S - (i+1)*3 + i
        cnt += C.comb(cur,i)
        cnt %= mod
    ans = cnt
    print(ans)
    return

def examE():
    N = I()
    CD = [[]for _ in range(2)]
    for i in range(N):
        x, y = LI()
        CD[0].append(x-y)
        CD[1].append(x+y)
    ans = max(max(CD[0]) - min(CD[0]),max(CD[1]) - min(CD[1]))
    print(ans)
    return

def examF():
    N = I()
    A = LI()
    B = LI()
    n = 0
    cur = 0
    prevA = 0
    prevB = 0
    curb = 1
    listcurb = [0]*N
    flag = False
    ib = 0
    for i in range(N):
        #print(flag,i)
        if flag:
            if prevA==A[i]:
                cur += 1
            else:
                flag = False
                if n<cur:
                    ib -= (cur-n)
                    n = deepcopy(cur)
                cur = deepcopy(n)
        else:
            if A[i]==B[ib]:
                #print(i,ib)
                flag = True
                cur = deepcopy(n) + 1
                if i==ib:
                    if prevB == B[ib]:
                        cur += curb
                else:
                    cur += listcurb[ib] - 1
        if prevB == B[i]:
            curb += 1
        else:
            curb = 1

        prevA = A[i]
        prevB = B[i]
        listcurb[i] = curb
        ib += 1

    if flag:
        n = max(cur,n)
    #print(n)
    #c = Counter(A)
    #print(c)
    #n = max(c.values())
    #print(n)
    ans = [0]*N
    for i in range(N):
        ans[i+n-N] = B[i]
    #print(ans)
    #print(listcurb)
    flag_tmp = False
    for i in range(N):
        if ans[i]==A[i]:
            n += 1
            flag_tmp = True
            break
    k = n
    while(flag_tmp and k<min(600,N-1)):
        flag_tmp = False
        k += 1
        for i in range(N):
            ans[i + n - N] = B[i]
        # print(ans)
        # print(listcurb)
        flag_tmp = False
        for i in range(N):
            if ans[i] == A[i]:
                n += 5
                flag_tmp = True
                break

    for i in range(N):
        if ans[i] == A[i]:
            print("No")
            return
    print("Yes")
    print(" ".join(map(str,ans)))
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
global mod,mod2,inf,alphabet,alphabet_convert,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 1<<31
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    main()

"""
6
5 5 5 5 5 6
1 5 6 7 7 7

6
2 3 5 5 5 6
1 5 6 7 7 7

6
2 3 5 5 5 6
3 3 6 7 7 7

6
2 2 3 3 3 5
3 3 3 7 7 7

6
1 1 2 3 3 3
2 2 2 3 3 3

6
3 3 3 4 4 5
1 1 3 4 4 4

7
1 2 2 3 3 3 3
2 2 3 3 3 4 4

7
1 2 2 2 2 3 3
1 2 3 3 3 4 4

10
1 2 2 3 3 3 4 4 4 4
1 2 3 4 5 5 5 5 5 5

6
1 1 2 3 4 5
1 3 5 5 5 5

"""