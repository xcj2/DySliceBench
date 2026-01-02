#!python3

import sys
sys.setrecursionlimit(10 ** 6)


def LI():
    return list(map(int, input().split()))

# input
N = int(input())
UVW = [LI() for _ in range(N - 1)]


# params
link = [[] for _ in range(N)]
for u, v, w in UVW:
    u -= 1
    v -= 1
    link[u].append((v, w))
    link[v].append((u, w))


def dfs(ans, x):
    for y, w in link[x]:
        if ans[y] is None:
            if w % 2 == 0:
                ans[y] = ans[x]
            else:
                ans[y] = 0 if ans[x] else 1
            dfs(ans, y)


def main():
    ans = [None] * N
    ans[0] = 0
    dfs(ans, 0)
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
