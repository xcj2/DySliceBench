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
from bisect import bisect_left

def main():
    N, Q = LI()
    XST = []
    for _ in range(N):
        s, t, x = LI()
        XST.append([x, s, t])
    D = []
    for _ in range(Q):
        D.append(II())
    ans = [-1] * Q
    nexts = [-1] * Q
    XST.sort()
    for x, s, t in XST:
        i = bisect_left(D, s - x)
        end = bisect_left(D, t - x)
        while i < end:
            if nexts[i] == -1:
                ans[i] = x
                nexts[i] = end
                i += 1
            else:
                i = nexts[i]
    for y in ans:
        print(y)
    return

main()
