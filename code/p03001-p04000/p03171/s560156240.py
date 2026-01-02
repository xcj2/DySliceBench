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

    n=int(data())
    A=list(mdata())
    dp=[[0]*n for i in range(n)]
    for i in range(n):
        dp[i][i]=A[i]
    for i in range(n):
        for j in range(i-1,-1,-1):
            dp[j][i]=max(A[j]-dp[j+1][i],A[i]-dp[j][i-1])
    print(dp[0][n-1])

if __name__ == '__main__':
    main()