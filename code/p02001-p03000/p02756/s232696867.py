import sys; sys.setrecursionlimit(2147483647); input = sys.stdin.readline
from math import floor, ceil, sqrt, factorial, log
from collections import Counter, defaultdict, deque
from operator import itemgetter
INF = float('inf'); MOD = 10**9+7
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(MI())
def LIR(n): return [LI() for i in range(n)]
def S(): return input().rstrip()
def LIR(n): return [S().split() for i in range(n)]

def main():
    s = S(); Q = I()
    mode = 2
    d = deque(s)

    for i in range(Q):
        query = S()
        if query[0] == "1": mode = 3 - mode
        else:
            t, f, c = map(str, query.split())
            if (int(f) + mode)% 2  == 0: d.append(c)
            else: d.appendleft(c)
    if mode == 2: print(''.join(d))
    else: print(''.join(list(d)[::-1]))

if __name__ == '__main__':
    main()