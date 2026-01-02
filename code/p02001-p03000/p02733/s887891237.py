#どっちで出すか注意, rstrip注意
#提出前に見返すこと！
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
    #mod = 10**9 + 7

    H,W,K = map(int, input().split())
    table = [list(map(int, list(input().rstrip()))) for _ in range(H)]
    

        #tableの累積和dを返す
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
    
    d = csum_gen(H, W, table)

    #座標(p, q)を含む長方形の和
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

    res = 10**15
    for i in range(2**(H-1)):
        tate = [0]
        for j in range(H-1):
            if i & 2**j:
                tate.append(j+1)
        l = len(tate)
        tate.append(H)
        start = 0
        cnt = 0
        flag = 0
        for j in range(W-1):
            for k in range(l):
                if K < csum_cal(tate[k], start, tate[k+1]-1, j, d):
                    flag = 1
            for k in range(l):
                if K < csum_cal(tate[k], start, tate[k+1]-1, j+1, d):
                    cnt += 1
                    start = j+1
                    break
            if flag:
                break
        else:
            res = min(res, cnt+l-1)
    print(res)




if __name__ == '__main__':
    main()
