def LI(): return [int(x) for x in input().split(" ")]
def LS(): return [str(x) for x in input().split(" ")]
def ItoS(L): return [str(x) for x in L]
def StoI(L): return [int(c) for c in L]


def solve():
    while 1:
        try:
            n = int(input())
            T, X, Y = [], [], []
            for _ in range(n):
                tmp1, tmp2, tmp3 = LI()
                T.append(tmp1)
                X.append(tmp2)
                Y.append(tmp3)

            T.insert(0, 0)
            X.insert(0, 0)
            Y.insert(0, 0)
            for i in range(n):
                if X[i + 1] == X[i] and Y[i + 1] == Y[i]:
                    raise EndLoop
                time = T[i + 1] - T[i]
                dis = abs(X[i + 1] - X[i]) + abs(Y[i + 1] - Y[i])
                if not ((time == dis) or (time > dis and (time - dis) % 2 == 0)):
                    raise EndLoop

            print("Yes")
            break
        except:
            print("No")
            break


solve()