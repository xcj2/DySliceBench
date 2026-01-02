from sys import stdin
from heapq import heappush, heappop

def ria(sep = ''):
    if sep == '' :
        return list(map(int, input().split())) 
    else: return list(map(int, input().split(sep)))
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def ri(): return int(input())
def rd(): return float(iuput())
def rs(): return input()

X, Y, Z, K = map(int, input().split())
A = ria()
B = ria()
C = ria()

A.sort()
A.reverse()
B.sort()
B.reverse()
C.sort()
C.reverse()

hp = []
heappush(hp, (-(A[0] + B[0] + C[0]), 0, 0, 0))
hs = set()
hs.add((0, 0, 0))
for k in range(K):
    p = heappop(hp)
    print(p[0] * -1)
    ix = p[1]
    iy = p[2]
    iz = p[3]
    if (ix + 1 < X) and ((ix + 1, iy, iz) not in hs):
        hs.add((ix + 1, iy, iz))
        heappush(hp,(-(A[ix + 1] + B[iy] + C[iz]), ix + 1, iy, iz))
    if iy + 1 < Y and ((ix, iy + 1, iz) not in hs):
        hs.add((ix, iy + 1, iz))
        heappush(hp,(-(A[ix] + B[iy + 1] + C[iz]), ix, iy + 1, iz))
    if iz + 1 < Z and ((ix, iy, iz + 1) not in hs):
        hs.add((ix, iy, iz + 1))
        heappush(hp,(-(A[ix] + B[iy] + C[iz + 1]), ix, iy, iz + 1))
