import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    INF = 10**18    

    # 最小消費MP
    def rec(i, a, b, c):# i:現在使った本数　a,b,c：現在の竹の長さ
        # 全て竹使ったら理想とのズレを魔法1,2で埋めてく
        if i == N:
            if not a or not b or not c:
                return INF
            return abs(a-A)+abs(b-B)+abs(c-C)
        
        # 竹不採用
        res = rec(i+1, a, b, c)
        # a採用
        if a >= 1:
            res = min(res, rec(i+1, a+L[i], b, c)+10)
        else:
            res = min(res, rec(i+1, a+L[i], b, c))
        # b採用
        if b >= 1:
            res = min(res, rec(i+1, a, b+L[i], c)+10)
        else:
            res = min(res, rec(i+1, a, b+L[i], c))
        
        # c採用
        if c >= 1:
            res = min(res, rec(i+1, a, b, c+L[i])+10)
        else:
            res = min(res, rec(i+1, a, b, c+L[i]))

        return res

    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]

    print(rec(0, 0, 0, 0))

resolve()