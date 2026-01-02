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
    R, G, B, N = LI()
    ans = 0
    for r in range(0, N+1, R):
        for g in range(0, N+1 - r, G):
            if (N - r - g) % B == 0:
                ans += 1
    return ans

print(main())