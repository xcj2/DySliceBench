'''
https://atcoder.jp/contests/abc106/tasks/abc106_d
'''
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 1000000007

    N,M,Q = map(int, input().split())
    table = [[0]*N for _ in range(N)]
    for _ in range(M):
        l,r = map(int, input().split())
        table[l-1][r-1] += 1

    def csum_gen(h, w, table):
        d = [[0]*w for _ in range(h)]
        d[0][0] = table[0][0]
        for i in range(1, w):
            d[0][i] = d[0][i-1]+table[0][i]
        #上のマスとその行の和を足す
        for i in range(1, h):
            total = 0
            for j in range(w):
                total += table[i][j]
                d[i][j] = d[i-1][j]+total
        return d

    d = csum_gen(N, N, table)

    def csum_cal(p, q, x, y, d):
        #p<=x and q<=y
        if p>x or q>y:
            return 0
        if p==0 and q==0:
            return d[x][y]
        if p==0:
            return d[x][y] - d[x][q-1]
        if q==0:
            return d[x][y] - d[p-1][y]
        return d[x][y]-d[p-1][y]-d[x][q-1]+d[p-1][q-1]


    for _ in range(Q):
        p,q = map(int, input().split())
        print(csum_cal(p-1, p-1, q-1, q-1, d))



if __name__ == '__main__':
    main()