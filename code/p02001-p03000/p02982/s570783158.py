import sys
import math
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
    
N,D=LI()
MAT=[LI() for i in range(N)]


cnt = 0
for i in range(N):
    for j in range(i+1, N):
        dist = 0
        for k in range(D):
            dist += (MAT[i][k]-MAT[j][k])*(MAT[i][k]-MAT[j][k])
        distrt = math.ceil(math.sqrt(dist))
        if distrt*distrt == dist:
            cnt += 1
print(cnt)
