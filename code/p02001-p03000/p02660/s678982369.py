import sys
import math
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1
PRIMES=[]

for p in gen_primes():
    if p < 1000000:
        PRIMES.append(p)
    else:
        break

N=II()
cnt = 0
for PR in PRIMES:
    for i in range(1,64):
        v = PR**i
        if N % v == 0:
            # print("PR:{} i:{}".format(PR, i))
            cnt += 1
            N //= v
            # print(N)
        else:
            while N % PR == 0: N //= PR
            break

# print(N)
if N > 1: cnt += 1
print(cnt)
