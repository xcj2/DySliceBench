'''
二部グラフ判定
'''
INFTY = 10**13
def floyd():
    for k in range(N):
        for i in range(N):
            if d[i][k] == INFTY:
                continue
            for j in range(N):
                if d[k][j] == INFTY:
                    continue
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

def dfs(v, c):
    color[v] = c
    for i in G[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    # ds[v] += d
    return True
def solve():
    for i in range(N):
        if color[i] == 0:
            if not dfs(i, 1):
                return False
    return True
N = int(input())
G = [[]for i in range(N)]
color = [0 for i in range(N)]
# ds = [1 for i in range(N)]
d = [[0 if i == j else INFTY for j in range(N)]for i in range(N)]
for i in range(N):
    S = input()
    for j, s in enumerate(S):
        if s == '1':
            G[i].append(j)
            d[i][j] = 1

ans = solve()
if ans:
    floyd()
    print(max([max(di)for di in d])+1)
    # print(max(ds))
else:
    print(-1)
