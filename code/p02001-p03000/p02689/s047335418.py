import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M = MI()
H = LMI()
nl = [list() for _ in range(N)]
for _ in range(M):
    a, b = MI()
    a -= 1
    b -= 1
    nl[a].append(b)
    nl[b].append(a)

ans = 0
for i in range(N):
    good = True
    for j in nl[i]:
        if H[i] <= H[j]:
            good = False
            break
    if good:
        ans += 1
print(ans)