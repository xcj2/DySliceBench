import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N, D, A = LI()
    X_H = []
    for _ in range(N):
        x, h = LI()
        X_H.append((x, h))
    X_H = sorted(X_H, key=lambda x:x[0])
    X = [elem[0] for elem in X_H]
    kaihuku = [0 for _ in range(N)]
    cur_damage = 0
    n_attack = 0
    cnt = 0
    for i in range(N):
        x, tairyoku = X_H[i]
        cur_damage = cur_damage - kaihuku[i]
        tairyoku -= cur_damage
        tairyoku = max(tairyoku, 0)
        n_attack = tairyoku // A + (tairyoku % A > 0)

        cur_damage += n_attack * A
        ins_pos = bisect.bisect_right(X, x + 2*D)
        if ins_pos < N:
            kaihuku[ins_pos] += n_attack * A
        cnt += n_attack

    print(cnt)

main()

