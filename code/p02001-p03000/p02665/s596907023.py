import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A = LMI()

M = [tuple() for _ in range(N + 1)]
for i, a in enumerate(reversed(A)):
    i = N - i
    if i == N:
        M[i] = (a, a)
    else:
        n, m = M[i + 1]
        M[i] = (-(-n // 2) + a, m + a)

if M[0][0] != 1:
    print(-1)
    exit(0)

ans = 1
par = 1
for i in range(1, N + 1):
    least, most = par, par * 2
    minv, maxv = M[i]
    v = min(maxv, most)
    ans += v
    par = v - A[i]
print(ans)