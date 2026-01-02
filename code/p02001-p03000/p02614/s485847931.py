import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


H, W, K = MI()
C = [input() for _ in range(H)]

def count(red_x, red_y):
    cnt = 0
    for i in range(H):
        if i in red_x:
            continue
        for j in range(W):
            if j in red_y:
                continue
            if C[i][j] == '#':
                cnt += 1
    return cnt

ans = 0
for i in range(2 ** H):
    red_x = []
    for j in range(H):
        if (i >> j) & 1:
            red_x.append(j)
    for k in range(2 ** W):
        red_y = []
        for l in range(W):
            if (k >> l) & 1:
                red_y.append(l)
        if count(red_x, red_y) == K:
            ans += 1
print(ans)