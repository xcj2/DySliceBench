import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

def main():
    N = II()
    S = []
    for _ in range(N):
        S.append(II())
    ans = sum(S)
    if ans % 10 == 0:
        m = INF
        for s in S:
            if s % 10:
                m = min(m, s)
        if m == INF:
            ans = 0
        else:
            ans -= m
    return ans

print(main())