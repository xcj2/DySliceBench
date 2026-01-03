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

def nt(n):
    if n == "1":
        return "0"
    else:
        return "1"

def check(seed, n, s):
    ans = seed
    for i in range(1, n):
        a, b = ans[-1], ans[-2]
        if int(s[i]) ^ int(b) == 0:
            ans.append(a)
        else:
            ans.append(nt(a))

    if ans[-1] != ans[0]:
        return []
    else:
        del(ans[-1])
        # print(ans)
        if int(s[0]) ^ int(ans[0]) == 0:
            if ans[-1] != ans[1]:
                return []
        else:
            if ans[-1] == ans[1]:
                return []

    return "".join(ans).replace("1", "S").replace("0", "W")

def solve():
    n = getN()
    S = getS()
    S = S.replace("o", "1").replace("x", "0")
    for seed in  [["1","1"], ["1","0"], ["0","1"], ["0","0"]]:
        ans = check(seed, n, S)
        if ans:
            print(ans)
            return

    print(-1)
    return

def main():
    n = getN()
    for _ in range(n):
        solve()
if __name__ == "__main__":
    # main()
    solve()
