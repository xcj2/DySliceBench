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
    s = []
    H, W = LI()
    for i in range(H):
        _s = S()
        s.append(_s)
    for r in range(H):
        for c in range(W):
            if s[r][c] == '.':
                continue
            any_tonari_black = False
            for dr, dc in zip(DR, DC):
                new_r = r + dr
                new_c = c + dc
                if not (0 <= new_r < H and 0 <= new_c < W):
                    continue
                if s[new_r][new_c] == '#':
                    any_tonari_black = True
            if not any_tonari_black:
                print('No')
                return
    print('Yes')
main()

