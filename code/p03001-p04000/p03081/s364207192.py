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
    N, Q = LI()
    s = SI()
    TD = []
    for _ in range(Q):
        TD.append(LS())
    rev = TD[::-1]
    l, r = -1, N
    for t, d in rev:
        if t == s[l + 1] and d == 'L':
            l += 1
        elif t == s[r - 1] and d == 'R':
            r -= 1
        if l > -1 and t == s[l] and d == 'R':
            l -= 1
        elif r < N and t == s[r] and d == 'L':
            r += 1
        if r == 0 or l == N - 1:
            break
    ans = max(0, r - l - 1)
    return ans

print(main())