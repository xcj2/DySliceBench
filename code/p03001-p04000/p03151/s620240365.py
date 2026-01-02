# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()


N = I()
A = LI()
B = LI()
if sum(A) < sum(B):
    print(-1)
    exit()

cnt = 0
need = 0
mochi = []
for i in range(N):
    a = A[i]
    b = B[i]
    if a < b:
        cnt += 1
        need += b - a
    else:
        mochi.append(a - b)

mochi.sort()
# print(cnt, need)
# print(mochi)

while need > 0:
    p = mochi.pop()
    need -= p
    cnt += 1

print(cnt)

