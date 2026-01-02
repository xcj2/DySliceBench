def main():

    from bisect import bisect_left as bl, bisect_right as br, insort
    import sys
    import heapq
    # from math import *
    from collections import defaultdict as dd, deque
    def data(): return sys.stdin.readline().strip()
    def mdata(): return map(int, data().split())
    out = sys.stdout.write
    # sys.setrecursionlimit(100000)

    n, k = mdata()
    a = list(mdata())
    dp = [0]*(k+1)
    for i in range(1, k + 1):
        for j in a:
            if i >= j:
                if dp[i - j] == 0:
                    dp[i] = 1
            if dp[i] == 1:
                break
    print("First" if dp[k] else "Second")


if __name__ == '__main__':
    main()