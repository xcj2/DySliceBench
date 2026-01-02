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
    W = LI()
    a = 0
    b = sum(W)
    ans = INF
    for w in W:
        ans = min(ans, abs(a - b))
        a += w
        b -= w
    ans = min(ans, abs(a - b))
    return ans

print(main())