import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

N = ii()
A = sorted(li())

if N%2==1:
    if A[0]!=0:
        print(0)
        exit()
    for i in range(1, N//2+1):
        i2 = i*2
        if A[i2-1]!=i2 or A[i2]!=i2:
            print(0)
            exit()

else:
    for i in range(N//2):
        i2 = i*2
        if A[i2]!=i2+1 or A[i2+1]!=i2+1:
            print(0)
            exit()

INF = 10**9+7
print(2**(N//2)%INF)