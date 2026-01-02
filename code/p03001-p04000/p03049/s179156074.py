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
        S.append(SI())
    ans = 0
    BA = 0
    BX = 0
    XA = 0
    for s in S:
        if s[0] == 'B' and s[-1] == 'A':
            BA += 1
        elif s[0] == 'B':
            BX += 1
        elif s[-1] == 'A':
            XA += 1
        for i in range(len(s) - 1):
            if s[i] == 'A' and s[i+1] == 'B':
                ans += 1
    ans += min(BA + BX, BA + XA)
    if BX == 0 and XA == 0 and BA > 0:
        ans -= 1
    return ans

print(main())
