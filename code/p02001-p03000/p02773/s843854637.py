import sys; sys.setrecursionlimit(2147483647); input = sys.stdin.readline
from math import floor, ceil, sqrt, factorial, log
from collections import Counter, defaultdict
from operator import itemgetter
INF = float('inf'); MOD = 10**9+7
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(MI())
def LIR(n): return [LI() for i in range(n)]
def S(): return input().rstrip()

def main():
    N = I()
    s = [S() for i in range(N)]    
    c = Counter(s).most_common()
    max_n = c[0][1]
    l = []
    for i in c:
        if i[1] == max_n:
            l.append(i[0])
    for i in sorted(l):
        print(i)
if __name__ == '__main__':
    main()
