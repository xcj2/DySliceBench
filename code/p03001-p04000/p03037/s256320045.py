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
    N, M = LI()
    LR = []
    for _ in range(M):
        LR.append(LI())
    left = 0
    right = INF
    for l, r in LR:
        left = max(left, l)
        right = min(right, r)
    ans = max(right - left + 1, 0)
    return ans

print(main())
