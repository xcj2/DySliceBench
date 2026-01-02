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
    N = len(S)
    S = reversed(S)
    dp = [[0 for j in range(13)] for i in range(N)]
 
    for i, es in enumerate(S):
        c = es
        if i == 0:
            if c == '?':
                for j in range(10):
                    dp[i][j] = 1
            else:
                dp[i][int(c)] = 1
        else:
            if c == '?':
                for j in range(10):
                    amari = (j * pow(10, i, 13)) % 13
                    for k in range(13):
                        dp[i][k] = (dp[i][k] + dp[i-1][(k-amari)%13]) % MOD
            else:
                amari = (int(c) * pow(10, i, 13)) % 13
                for k in range(13):
                    dp[i][k] += (dp[i][k] + dp[i - 1][(k-amari) % 13]) % MOD
 
    dprint(dp)
    print(dp[N-1][5])


solve()