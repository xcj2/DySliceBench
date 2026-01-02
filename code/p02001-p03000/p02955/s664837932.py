inf = float('inf')

from math import floor
# 約数全列挙(ソート済み)
# n = 24 -> [1,2,3,4,6,8,12,24]
def divisor(n):
    left = [1]
    right = [n]
    sup = floor(pow(n,1/2))
    for p in range(2,sup+1):
        if n % p == 0:
            if p == n//p:
                left.append(p)
                continue
            left.append(p)
            right.append(n//p)
    res = left + right[::-1]
    return res

def accmulate(array):
    global cs
    cs = [0]*(len(array)+1)
    for i in range(len(array)):
        cs[i+1] = cs[i] + array[i]

def query(l,r):
    return cs[r] - cs[l]

N,K = map(int,input().split())
A = list(map(int,input().split()))
sA = sorted(A)

S = sum(A)
for d in divisor(S)[::-1]:
    nA = sorted([a % d for a in A])
    accmulate(nA)
    cnt = inf
    for i in range(N+1):
        minus = -query(0,i)
        plus = d*(N-i) - query(i,N)
        if minus + plus == 0:
            cnt = min(cnt, plus)
    if cnt <= K:
        print(d)
        exit()