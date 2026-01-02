import sys
input = sys.stdin.readline

INF = 10**18

N = int(input())
X = [0] * N
Y = [0] * N
U = [''] * N
for i in range(N):
    x, y, u = input().split()
    X[i] = int(x)
    Y[i] = int(y)
    U[i] = u
M = 200000

def rotate():
    s = 'ULDR'
    for i in range(N):
        X[i], Y[i] = M - Y[i], X[i]
        U[i] = s[(s.index(U[i]) + 1) % 4]

def calc1():
    v = [[] for _ in range(M+1)]
    for x, y, u in zip(X, Y, U):
        if u in 'RL':
            v[y].append((x, u))
    ret = INF
    for y in range(M+1):
        v[y].sort(key=lambda p: p[0])
        for i in range(len(v[y])-1):
            if v[y][i][1] == 'R' and v[y][i+1][1] == 'L':
                ret = min(ret, (v[y][i+1][0] - v[y][i][0]) * 5)
    return ret

def calc2():
    v = [[] for _ in range(2*M+1)]
    for x, y, u in zip(X, Y, U):
        if u in 'UR':
            v[x+y].append((x, u))
    ret = INF
    for xy in range(2*M+1):
        v[xy].sort(key=lambda p: p[0])
        for i in range(len(v[xy])-1):
            if v[xy][i][1] == 'R' and v[xy][i+1][1] == 'U':
                ret = min(ret, (v[xy][i+1][0] - v[xy][i][0]) * 10)
    return ret

ans = INF
for i in range(4):
    ans = min(ans, calc1(), calc2())
    rotate()
print(ans if ans < INF else 'SAFE')