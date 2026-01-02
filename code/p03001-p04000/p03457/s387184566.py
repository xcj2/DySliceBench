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
def pf(s): return print(s, flush=True)

N = I()
txy = []
for i in range(N):
    txy.append(LI())

txy = sorted(txy, key=lambda x:x[0])
#  print(txy)
count = 0
current = [0,0]
for item in txy:
    #  print(count, current)
    dist = abs(current[0] - item[1]) + abs(current[1] - item[2])
    if dist > item[0] - count:
        # 足らず
        print('No')
        exit()
    elif dist == item[0] - count:
        # ちょうど
        count = item[0]
        current = [item[1], item[2]]
    else:
        # 余り
        rest = item[0] - count - dist
        count = item[0]
        current = [item[1], item[2]]
        #  print('rest', rest)
        if rest % 2 != 0:
            # いけない
            print('No')
            exit()
print("Yes")


