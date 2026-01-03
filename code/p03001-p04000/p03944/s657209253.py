def LI(): return [int(x) for x in input().split(" ")]
def LS(): return [str(x) for x in input().split(" ")]
def ItoS(L): return [str(x) for x in L]
def StoI(L): return [int(c) for c in L]


def solve():
    w, h, n = LI()
    X, Y, A = [], [], []
    for _ in range(n):
        tmp1, tmp2, tmp3 = LI()
        X.append(tmp1)
        Y.append(tmp2)
        A.append(tmp3)

    field = [[1 for _ in range(w)] for __ in range(h)]

    for i, a in enumerate(A):
        if a == 1:
            for j in range(X[i]):
                for k in range(h):
                    field[k][j] = 0
        elif a == 2:
            for j in range(X[i], w):
                for k in range(h):
                    field[k][j] = 0
        elif a == 3:
            for j in range(Y[i]):
                for k in range(w):
                    field[j][k] = 0
        elif a == 4:
            for j in range(Y[i], h):
                for k in range(w):
                    field[j][k] = 0
        else:
            pass
        
    ans = 0
    for ele in field:
        ans += ele.count(1)

    print(ans)


solve()