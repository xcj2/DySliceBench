def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors
def examA():
    M, D = LI()
    c = D//10
    ans = 0
    for i in range(2,M+1):
        d = make_divisors(i)
#        print(d)
        for j in range(len(d)//2):
            cur0 = d[j*2+1]; cur10 = d[j*2]
            if cur10==1:
                continue
            if cur0<=9:
                if cur10<c:
                    ans +=1
#                    print(cur10,cur0)
                elif cur10==c and cur0+cur10*10<=D:
                    ans +=1
#                    print(cur10,cur0)
        for j in range(len(d) // 2):
            cur0 = d[j * 2];cur10 = d[j * 2+1]
            if cur0 == 1:
                continue
            if cur10 <= 9:
                if cur10 < c:
                    ans += 1
                elif cur10 == c and cur0 + cur10 * 10 <= D:
                    ans += 1
        if len(d)%2==1:
            cur0 = d[-1]; cur10 = d[-1]
            if cur10==1:
                continue
            if cur0<=9:
                if cur10<c:
                    ans +=1
#                    print(cur10,cur0)
                elif cur10==c and cur0+cur10*10<=D:
                    ans +=1
#                    print(cur10,cur0)
    print(ans)
    return

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
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
        return
def examB():
    N, K = LI()
    A = LI()
    bit = Bit(max(A))
    cur = 0
    for i, a in enumerate(A):
        bit.add(a, 1)
        cur += i + 1 - bit.sum(a)
    As = 0
    A.sort()
    now = 0
    for i in range(1,N):
        if A[i]!=A[i-1]:
            now = i
        As += now
#    print(cur,As)
    ans = (As*(K**2) - (As-2*cur)*K)//2
    ans %=mod
    print(ans)
    return

def examC():
    N = I()
    S = SI()
    L = [0]; R= []
    flagL = True
    for i in range(1,2*N):
        if S[i]==S[i-1]:
            if flagL:
                R.append(i)
                flagL = False
            else:
                L.append(i)
                flagL = True
        else:
            if flagL:
                L.append(i)
                flagL = True
            else:
                R.append(i)
                flagL = False
#    print(L); print(R)
    if len(L)!=N or S[0]=="W" or S[-1]=="W":
        print("0")
        return
    cur = 1
    sumR = [0]*(2*N)
    now = 0
    for k,i in enumerate(R):
        for j in range(now,i):
            sumR[j] = k
        now = i
#    print(sumR)
    for i in range(N-1,-1,-1):
        cur *=(N-sumR[L[i]]-(N-i-1))
#        print(cur,L[i])
        cur %=mod
#    print(cur)
    for i in range(N):
        cur *=(i+1)
        cur %=mod
    ans = cur
    print(ans)
    return

def examE():
    N, H, W = LI()
    d = defaultdict(list)
    HL = [[]for _ in range(H+1)]
    WL = [[]for _ in range(W+1)]
    for _ in range(N):
        r,c,a = LI()
        d[(r,c)].append(a)
        HL[r].append(-a)
        WL[c].append(-a)
    print(d)

    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,inf
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examC()
