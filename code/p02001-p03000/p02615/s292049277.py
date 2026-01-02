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

N=II()
AS=LI()
AS.sort(reverse=True)
# print(AS)

i, j = AS[0], AS[1]
HQ=[]
heapq.heappush(HQ, (-i, -j))
heapq.heappush(HQ, (-i, -j))
# print(HQ)
res = AS[0]
for n in range(2, len(AS)):
    k = AS[n]
    i, j = heapq.heappop(HQ)
    i *= -1
    j *= -1
    res += min(i, j)
    heapq.heappush(HQ, (-k, -i))
    heapq.heappush(HQ, (-k, -j))
    # print("i: {} j: {} k:{} res:{}".format(i,j,k,res))
    # print(HQ)

print(res)
