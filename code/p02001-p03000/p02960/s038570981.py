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

debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def solve():
    S = SI()
    S = S[::-1]
    N = len(S)
    dp = [0 for j in range(13)]
    dp2 = [0 for j in range(13)]

    for i, c in enumerate(S):
        if i == 0:
            if c == '?':
                for j in range(10):
                    dp[j] = 1
            else:
                dp[int(c)] = 1
        else:
            if c == '?':
                for j in range(10):
                    amari = (j * pow(10, i, 13)) % 13
                    for k in range(13):
                        dp2[k] = (dp2[k] + dp[(k-amari)%13]) % MOD
            else:
                for k in range(13):
                    amari = (int(c) * pow(10, i, 13)) % 13
                    dp2[k] = (dp2[k] + dp[(k-amari) % 13]) % MOD

            dp = dp2
            dp2 = [0 for j in range(13)]

    dprint(dp)
    print(dp[5])



solve()