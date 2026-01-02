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
    A = []
    for _ in range(M):
        A.append(II())
    A.append(INF)
    pre = 0
    cur = 1
    k = 0
    for i in range(1, N + 1):
        if i == A[k]:
            k += 1
            pre = cur
            cur = 0
        else:
            tmp = cur
            cur = (cur + pre) % MOD
            pre = tmp
    ans = cur
    return ans

print(main())