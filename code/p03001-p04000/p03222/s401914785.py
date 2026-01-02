import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

h,w,k = li()
k -= 1
MOD = 10**9 + 7

# 遷移行列
if w > 1:
    matrix = [[0]*w for _ in range(w)]
    for num in range(1 << (w-1)):
        if "11" in bin(num):
            continue

        ex = False
        for i, bit in enumerate(bin(num)[2:].zfill(w-1)):
            if bit == "1":
                ex = True
                matrix[i][i+1] += 1
                matrix[i+1][i] += 1

            elif ex:
                ex = False

            else:
                matrix[i][i] += 1

        if not ex:
            matrix[w-1][w-1] += 1

    # 適用
    dp = [1] + [0]*(w-1)
    for hi in range(h):
        nex = [0]*w
        for wj in range(w):
            for wk in range(w):
                nex[wj] += matrix[wj][wk] * dp[wk]
                nex[wj] %= MOD

        dp = nex

    print(dp[k])

else:
    print(1)