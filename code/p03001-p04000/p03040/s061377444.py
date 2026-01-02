import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


from heapq import heappush, heappop


# 中央値以上と以下をheapで管理
upper_asc = []
lower_dsc = []

q = ni()
ans = 0

for i in range(q):
    query = list(map(int, ns().split()))
    if query[0] == 1:
        a, b = query[1], query[2]
        heappush(upper_asc, a)
        heappush(lower_dsc, -a)

        if i == 0:
            ans += b
            continue

        x, y = heappop(upper_asc), -heappop(lower_dsc)

        ans += (y - x) + b

        heappush(upper_asc, y)
        heappush(lower_dsc, -x)

    else:
        print(-lower_dsc[0], ans)

