import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools


sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

N = I()
xyh = []
for i in range(N):
    x, y, h = LI()
    xyh.append([x,y,h])


for i in range(100+1):
    for j in range(100+1):
        cx, cy = i, j
        H = []
        for item in xyh:
            #  print(item)
            if item[2] == 0:
                continue

            new_H = max(item[2] + abs(item[0] - cx) + abs(item[1] - cy), 0)
            H.append(new_H)
        else:
            if len(set(H)) == 1:
                center_H = H[0]
                H = []
                for item in xyh:
                    if item[2] == 0:
                        # 0の場合にも正しいか判定する
                        # 中央の高さ
                        if center_H - abs(item[0] - cx) - abs(item[1] - cy) > 0:
                        #  if ch < center_H:
                            break
                else:
                    print(i, j, center_H)
                    exit()
