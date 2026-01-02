import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


H,W = MI()
a = [LS2() for _ in range(H)]

from collections import defaultdict

d = defaultdict(int)
for i in range(H):
    for j in range(W):
        d[a[i][j]] += 1

if H % 2 == 0 and W % 2 == 0:
    for key in d.keys():
        if d[key] % 4 != 0:
            print('No')
            exit()
    print('Yes')

if H % 2 == 0 and W % 2 != 0:
    H,W = W,H

if H % 2 != 0 and W % 2 == 0:
    a = 0
    for key in d.keys():
        if d[key] % 2 != 0:
            print('No')
            exit()
        elif d[key] % 4 != 0:
            a += 1
    if a <= W//2:
        print('Yes')
        exit()
    else:
        print('No')
        exit()

if H % 2 != 0 and W % 2 != 0:
    a,b = 0,0
    for key in d.keys():
        if d[key] % 4 == 1:
            a += 1
        elif d[key] % 4 == 3:
            a += 1
            b += 1
        elif d[key] % 4 == 2:
            b += 1
    if a <= 1 and b <= H//2 + W//2:
        print('Yes')
        exit()
    else:
        print('No')
        exit()
