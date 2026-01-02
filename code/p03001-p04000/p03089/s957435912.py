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
    B = LI()
    for i, b in enumerate(B, 1):
        if b > i:
            print(-1)
            return -1
    ans = [0] * N
    nofill = list(range(N))
    for b in B[::-1]:
        ans[nofill[b - 1]] = b
        del nofill[b - 1]
    for a in ans:
        print(a)

    return 0

main()