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
import numpy

def main():
    H, W = LI()
    S = []
    for i in range(H):
        S.append(list(SI()))
    S = (numpy.array(S) == '.')
    L = numpy.zeros((H, W), dtype=int)
    R = numpy.zeros((H, W), dtype=int)
    T = numpy.zeros((H, W), dtype=int)
    B = numpy.zeros((H, W), dtype=int)
    for i in range(H):
        L[i] = (L[i - 1] + 1) * S[i]
        R[-1 - i] = (R[-i] + 1) * S[-1 - i]
    for i in range(W):
        T[:, i] = (T[:, i - 1] + 1) * S[:, i]
        B[:, -1 - i] = (B[:, -i] + 1) * S[:, -1 - i]
    ans = numpy.max(L + R + T + B) - 3
    return ans

print(main())