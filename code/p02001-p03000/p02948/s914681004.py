import sys
import heapq
from collections import defaultdict

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    n, m = LI()
    c = defaultdict(list)
    for i in range(n):
        a, b = LI()
        c[a].append(b)
    # s_d = dict(sorted(d.items, key=lambda x: x[1]))
    s = []
    ans = 0
    for i in range(1, m+1):
        for j in c[i]:
            heapq.heappush(s, -j)
        if len(s) > 0:
            ans -= heapq.heappop(s)
    print(ans)

if __name__ == '__main__':
    main()