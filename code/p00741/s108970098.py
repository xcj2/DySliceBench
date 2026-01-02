import sys

sys.setrecursionlimit(2 * 10**6)


def inpl():
    return list(map(int, input().split()))


def solve(mp, w, h):
    def dfs(ny, nx):
        if mp[ny][nx] == 0:
            flag[ny][nx] = -1
            return
        elif visit[ny * w + nx]:
            return
        visit[ny * w + nx] = True

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                elif mp[ny + dy][nx + dx] == 0:
                    continue
                flag[ny + dy][nx + dx] = min(flag[ny][nx], flag[ny + dy][nx + dx])
                dfs(ny + dy, nx + dx)

    mp = [[0] + m + [0] for m in mp]
    mp = [[0] * (w + 2)] + mp + [[0] * (w + 2)]
    flag = [[-1] + [i + j * w for i in range(w)] + [-1] for j in range(h)]
    flag = [[-1] * (w + 2)] + flag + [[-1] * (w + 2)]
    visit = [False] * (w + 2) * (h + 2)

    for ny in range(h):
        for nx in range(w):
            dfs(ny + 1, nx + 1)
    # print(flag)

    ret = []
    for f in flag:
        ret += [i for i in f if i != -1]
    return len(set(ret))


ans = []
while True:
    w, h = inpl()
    if w == h == 0:
        break
    tmp = [inpl() for i in range(h)]
    ans.append(solve(tmp, w, h))

for a in ans:
    print(a)

