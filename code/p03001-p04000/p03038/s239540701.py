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
from collections import defaultdict
from operator import itemgetter

def main():
    N, M = LI()
    A = LI()
    BC = []
    for _ in range(M):
        BC.append(LI())
    for a in A:
        BC.append([1, a])
    BC.sort(reverse=True, key=itemgetter(1))
    cnt = 0
    ans = 0
    for B, C in BC:
        if cnt + B >= len(A):
            ans += C * (len(A) - cnt)
            break
        ans += C * B
        cnt += B
    return ans

print(main())