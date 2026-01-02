# Import
from collections import deque

# I/O
def read(): return input()
def read_int(): return int(input())
def read_array(type=int): return list(map(type, input().split()))
def read_tupple(type=None):
    tmp = input().split()
    if type is None: return map(int, tmp)
    assert len(tmp) == len(type)
    return [type[i](tmp[i]) for i in range(len(tmp))]

# Implementation
class PrimeNumber:
    def __init__(self, N):
        self.N = N
        self.isP, self.P = self.compute(N)

    def compute(self, N):
        isP, P = [True] * (N + 1), []
        for i in range(2, N+1):
            if isP[i]:
                P.append(i)
                for j in range(2*i, N+1, i):
                    isP[j] = False
        return isP, P

N = read_int()

pn = PrimeNumber(1000006)
ans = 0
for p in pn.P:
    cnt = 0
    while N % p == 0:
        N /= p
        cnt += 1
    dec = 1
    while cnt >= dec:
        cnt -= dec
        dec += 1
        ans += 1
if N > 1:
    ans += 1
print(ans)