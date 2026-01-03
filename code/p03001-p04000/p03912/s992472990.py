import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

# Mの倍数から優先的に作る

N,M = LI()
X = LI()

d = defaultdict(int)
dmod = defaultdict(int)
pair = defaultdict(int)

for i in range(N):
    d[X[i]] += 1
    m = X[i]%M
    dmod[m] += 1
    if d[X[i]]%2 == 0:
        pair[m] += 1

ans = dmod[0]//2
for i in range(1,(M+1)//2):
    a = dmod[i]
    b = dmod[M-i]
    if a <= b:
        ans += a + min((b-a)//2, pair[M-i])
    else:
        ans += b + min((a-b)//2, pair[i])
if M%2 == 0:
    ans += dmod[M//2]//2

print(ans)