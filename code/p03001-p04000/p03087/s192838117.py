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

from itertools import accumulate

def main():
    N, Q = LI()
    S = SI()
    LR = []
    for _ in range(Q):
        LR.append(LI_())

    AC = [0] * (N + 1)
    for i in range(N - 1):
        if S[i:i + 2] == 'AC':
            AC[i] = 1
    acc = [0] + list(accumulate(AC))
    for l, r in LR:
        print(acc[r] - acc[l])

    return 0

main()
