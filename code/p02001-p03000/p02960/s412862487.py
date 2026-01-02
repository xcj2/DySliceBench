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


from functools import lru_cache


def main(): 
    S = SI()

    # 桁DP
    dp_table = [[0 for _ in range(13)] for _ in range(len(S))]

    # 最初の桁を見る。
    if S[0] == '?':
        for i in range(10):
            dp_table[0][i] = 1
    else:
        dp_table[0][int(S[0])] = 1

    # 以降の桁を見ていく。
    for digit in range(1, len(S)):
        if S[digit] == '?':
            for prev_res, comb in enumerate(dp_table[digit-1]):
                for x in range(10):
                    res = (prev_res*10+x)%13
                    dp_table[digit][res] = (dp_table[digit][res] + comb)%MOD

        else:
            for prev_res, comb in enumerate(dp_table[digit-1]):
                res = (prev_res*10+int(S[digit]))%13
                dp_table[digit][res] = (dp_table[digit][res] + comb)%MOD

    print(dp_table[len(S)-1][5])





main()