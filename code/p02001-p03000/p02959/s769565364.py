import math
import sys
MAX_INT = int(10e9)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
a = IL()
b = IL()

ans = 0
for i in range(N):
    if a[i] <= b[i]:
        ans += a[i]
        b[i] -= a[i]
        if a[i+1] <= b[i]:
            ans += a[i+1]
            a[i+1] = 0
        else:
            ans += b[i]
            a[i+1] -= b[i]
    else:
        ans += b[i]

print(ans)