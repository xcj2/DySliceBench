import sys
# from collections import defaultdict, deque
# import math
# import copy
# from bisect import bisect_left, bisect_right
# import heapq

# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 1000000007

def dfs(n, s):
    if s:
        num = int(s)
        if num > n:
            return 0

    tmp = 0
    if "3" in s and "5" in s and "7" in s:
        # print(s)
        tmp += 1
    tmp += dfs(n, s + "3")
    tmp += dfs(n, s + "5")
    tmp += dfs(n, s + "7")
    return tmp


def solve():
    n = getN()
    ans = dfs(n, "")
    print(ans)

def main():
    n = getN()
    for _ in range(n):
        solve()
if __name__ == "__main__":
    # main()
    solve()
