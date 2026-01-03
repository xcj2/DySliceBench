# -*- coding: utf-8 -*-

import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

H, W = MAP()

if H%3==0 or W%3==0:
    print(0)
    exit()

H, W = max(H, W), min(H, W)

a = H // 3
bc = H - a
ans1 = max(abs(bc*ceil(W, 2)-a*W), abs(bc*(W//2)-a*W))
a = ceil(H, 3)
bc = H - a
ans2 = max(abs(bc*ceil(W, 2)-a*W), abs(bc*(W//2)-a*W))

H, W = min(H, W), max(H, W)

a = H // 3
bc = H - a
ans3 = max(abs(bc*ceil(W, 2)-a*W), abs(bc*(W//2)-a*W))
a = ceil(H, 3)
bc = H - a
ans4 = max(abs(bc*ceil(W, 2)-a*W), abs(bc*(W//2)-a*W))

ans5 = abs(ceil(W, 3)*H-W//3*H)
ans6 = abs(ceil(H, 3)*W-H//3*W)

print(min(ans1, ans2, ans3, ans4, ans5, ans6))
