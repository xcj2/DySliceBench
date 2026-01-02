import sys
from operator import xor
from functools import reduce
readline = sys.stdin.readline

mod = 10**18+3
base = 10**9+9
def rollinghash(S):
    N = len(S)
    has = [0]*(N+1)
    power = [1]*(N+1)
    for i in range(N):
        s = S[i]
        has[i+1] = (has[i]*base + s)%mod
        power[i+1] = power[i]*base%mod
    return has, power
 
def rh(i, j):
    return (has[j] - has[i]*power[j-i])%mod

def rotate(k):
    pass

N = int(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))
CA = [a1^a2 for a1, a2 in zip(A, A[1:])]
CA.append(A[0]^A[-1])
CB = [a1^a2 for a1, a2 in zip(B, B[1:])]
CB.append(B[0]^B[-1])

rA = [1+ca for ca in CA]
has, power = rollinghash(rA)
R = rh(0, N)
    
HA = [None]*N
suf = pow(base, N-1, mod)
for i in range(N):
    HA[i] = R
    R = ((R-suf*rA[i])*base + rA[i])%mod

rB = [1+cb for cb in CB]
has, power = rollinghash(rB)
R = rh(0, N)

Ans = []
for i in range(N):
    if HA[i] == R:
        Ans.append((i, A[i]^B[0]))

if Ans:
    print('\n'.join(' '.join(map(str, a)) for a in Ans))
