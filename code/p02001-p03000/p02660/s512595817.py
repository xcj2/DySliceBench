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
        self.compute()

    def compute(self):
        self.isP, self.P = [True] * (self.N + 1), []
        for i in range(2, self.N+1):
            if self.isP[i]:
                self.P.append(i)
                for j in range(2*i, self.N+1, i):
                    self.isP[j] = False

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