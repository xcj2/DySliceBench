import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)


def zaatsu(nums):
    ref = list(set(copy.copy(nums)))
    ref.sort()
    dic = dict()
    for i, num in enumerate(ref):
        dic[num] = i

    return [dic[num] for num in nums]

def solve():
    n, d, a = getList()
    li = []
    for i in range(n):
        li.append(getList())

    li.sort()
    ichi = [x[0] for x in li]
    imos = [0] * n
    cur = 0
    ans = 0
    for i, (x, h) in enumerate(li):
        cur -= imos[i]
        hp = h - cur * a
        if hp <= 0:
            continue
        thr = hp // a
        if hp % a != 0:
            thr += 1
        ans += thr
        cur += thr
        owari = bisect_right(ichi, x + 2 * d)
        if owari != n:
            imos[owari] += thr

    print(ans)
def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()





