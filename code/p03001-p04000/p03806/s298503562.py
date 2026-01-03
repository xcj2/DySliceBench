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

N,Ma,Mb = LI()
a,b,c = LIR(N,3)

n = N//2

d1 = [[5000]*401 for _ in range(401)]
d2 = [[5000]*401 for _ in range(401)]

for bit in range(1<<n):
    val_a = 0
    val_b = 0
    cost = 0
    for i in range(n):
        if bit>>i&1:
            val_a += a[n-1-i]
            val_b += b[n-1-i]
            cost += c[n-1-i]
    d1[val_a][val_b] = min(d1[val_a][val_b],cost)

for bit in range(1<<(N-n)):
    val_a = 0
    val_b = 0
    cost = 0
    for i in range(N-n):
        if bit>>i&1:
            val_a += a[N-1-i]
            val_b += b[N-1-i]
            cost += c[N-1-i]
    d2[val_a][val_b] = min(d2[val_a][val_b],cost)


vals = []
now = 1
while True:
    if Ma*now <= sum(a) and Mb*now <= sum(b):
        vals.append((Ma*now,Mb*now))
        now += 1
    else:
        break

ans = 5000
for ka in range(401):
    for kb in range(401):
        if d1[ka][kb] != 5000:
            for v in vals[::-1]:
                left_a = v[0]-ka
                left_b = v[1]-kb
                if left_a < 0 or left_b < 0:
                    break
                if d1[ka][kb]+d2[left_a][left_b] < ans:
                    ans = d1[ka][kb]+d2[left_a][left_b]

if ans == 5000:
    print(-1)
else:
    print(ans)