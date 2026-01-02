import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main():
    H, W = LI()
    S = []
    for _ in range(H):
        S.append(SI())

    # print(S)

    # 横方向に探索
    yoko = [ [-1]*W for _ in range(H)]
    for i in range(H):
        beginning = True
        continuous = 0
        for j in range(W):
            if beginning:
                if S[i][j] == '#':
                    continue
                if S[i][j] == '.':
                    beginning = False
                    continuous += 1
            else:
                if S[i][j] == '#':
                    for k in range(j-continuous, j):
                        yoko[i][k] = continuous
                    beginning = True
                    continuous = 0
                if S[i][j] == '.':
                    continuous += 1
        if continuous:
            for k in range(W-continuous, W):
                yoko[i][k] = continuous

    # 縦方向に探索
    tate = [ [-1]*W for _ in range(H)]
    for j in range(W):
        beginning = True
        continuous = 0
        for i in range(H):
            if beginning:
                if S[i][j] == '#':
                    continue
                if S[i][j] == '.':
                    beginning = False
                    continuous += 1
            else:
                if S[i][j] == '#':
                    for k in range(i-continuous, i):
                        tate[k][j] = continuous
                    beginning = True
                    continuous = 0
                if S[i][j] == '.':
                    continuous += 1
        if continuous:
            for k in range(H-continuous, H):
                tate[k][j] = continuous

    ans = 1  # ぜったい1マスは光る。
    for i in range(H):
        for j in range(W):
            ans = max(ans, tate[i][j] + yoko[i][j] - 1)

    print(ans)

main()