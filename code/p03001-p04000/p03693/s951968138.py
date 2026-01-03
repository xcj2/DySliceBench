#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    n, m, R = LI()
    r = LI_()
    edg = [[inf] * n for i in range(n)]
    for _ in range(m):
        a, b, c = LI_()
        c += 1
        edg[a][b] = c
        edg[b][a] = c
    for i in range(n):
        edg[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                edg[i][j] = min(edg[i][j], edg[i][k] + edg[k][j])
    fulls = itertools.permutations(range(R), R)
    ans = inf
    for full in fulls:
        b = -1
        tmp = 0
        for f in full:
            if b == -1:
                b = r[f]
                continue
            tmp += edg[r[f]][b]
            b = r[f]
        ans = min(ans, tmp)
    print(ans)

    return

#B
def B():
    n, m = LI()
    time = [[inf] * n for i in range(n)]
    for _ in range(m):
        a, b, t = LI_()
        t += 1
        time[a][b] = t
        time[b][a] = t
    for i in range(n):
        time[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                time[i][j] = min(time[i][j], time[i][k] + time[k][j])
    for k in range(n):
        for i in range(n):
            if time[i][k] == inf:
                time[i][k] = 0
    ans = inf
    for i in range(n):
        ans = min(ans, max(time[i]))
    print(ans)
    return

#C
def C():
    h, w, t = LI()
    s = SR(h)
    for i in range(h):
        for k in range(w):
            if s[i][k] == "S":
                start = (i, k)
            if s[i][k] == "G":
                goal = (i, k)

    def f(X):
        dist = [[inf] * w for i in range(h)]
        dist[start[0]][start[1]] = 0
        q = [[0, start]]
        while q:
            # print(q,1)
            time, a = heappop(q)
            y, x = a
            for yi, xi in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                yi += y
                xi += x
                # print(yi,xi)
                if 0 <= yi < h and 0 <= xi < w:
                    if s[yi][xi] == "#":
                        if dist[yi][xi] > time + X:
                            heappush(q, [time + X, [yi, xi]])
                            dist[yi][xi] = time + X
                    else:
                        if dist[yi][xi] > time + 1:
                            heappush(q, [time + 1, [yi, xi]])
                            dist[yi][xi] = time + 1
        # print(dist)
        return dist[goal[0]][goal[1]]

    ok = 1
    ng = t + 1
    # print(goal)
    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if f(mid) <= t:
            ok = mid
        else:
            ng = mid
        # print(mid)
    print(ok)
    return

#D
def D():
    n = II()
    a, b = LI_()
    m = II()
    xy = [[] for i in range(n)]
    for _ in range(m):
        x, y = LI_()
        xy[x].append(y)
        xy[y].append(x)
    d = [inf] * n
    d[a] = 0
    q = [[0, a]]
    while q:
        dist, now = heappop(q)
        for i in xy[now]:
            if d[i] > dist + 1:
                heappush(q, (dist + 1, i))
                d[i] = dist + 1
    ans = 1
    q = [b]
    while q:
        qi = q[::1]
        q = []
        tmp = 0
        while qi:
            x = qi.pop()
            score = d[x]
            for xi in xy[x]:
                if d[xi] + 1 == score and not xi in q:
                    q.append(xi)
                    # print(tmp)
                    tmp += 1
        # print(tmp)
        ans *= tmp  
        ans %= mod
        q = list(set(q))
        # print(q)
        if q[0] == a:
            break
    print(ans)
    return

#E
def E():
    x = S()
    f = True
    while f and x:
        f = False
        if len(x) >= 2:
            if x[-1] == "h" and x[-2] == "c":
                x = x[:-2]
                f = True
                continue
        if x[-1] == "o":
            x = x[:-1]
            f = True
        elif x[-1] == "k":
            x = x[:-1]
            f = True
        elif x[-1] == "u":
            x = x[:-1]
            f = True
        # print(x)
    if f:
        print("YES")
    else:
        print("NO")
    return

#F
def F():
    s = S()
    n = II()
    for i in range(n):
        l, r = LI_()
        s[l: r + 1] = s[l: r + 1][::-1]
    print("".join(s))
    return

#G
def G():
    s = S()
    ans = []
    i = 0
    while i  < len(s):
        ans.append(s[i])
        tmp = 0
        x = s[i]
        while i != len(s):
            if x == s[i]:
                tmp += 1
                i += 1
                continue
            break
        ans.append(str(tmp))
    print("".join(ans))
    return

#H
def H():
    r, g, b = LI()
    if g & 1 and b % 4 == 2:
        print("YES")
        return
    if not (g & 1) and b % 4 == 0:
        print("YES")
        return
    print("NO")
    return

#Solve
if __name__ == '__main__':
    H()
