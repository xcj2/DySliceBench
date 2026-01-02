import sys
sys.setrecursionlimit(1000000000)
from itertools import count
from functools import lru_cache
from collections import defaultdict
ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
INF = float('inf')
def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok
#


def main():
    X = ii()
    @lru_cache(maxsize=None)
    def rec(n):
        if n == 0:
            return True
        elif n < 0:
            return False
        else:
            return any(rec(n-i) for i in range(100, 105+1))
    
    print(int(rec(X)))




main()
