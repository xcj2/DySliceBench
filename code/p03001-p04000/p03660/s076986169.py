#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, a: "List[int]", b: "List[int]"):
    conn = [[] for _ in range(N)]
    for i in range(N - 1):
        conn[a[i] - 1].append(b[i] - 1)
        conn[b[i] - 1].append(a[i] - 1)

    def dfs(idx, cur, conn, dis):
        dis[idx] = cur
        for nex in conn[idx]:
            if dis[nex] is None:
                dfs(nex, cur + 1, conn, dis)
        return None

    f_dis = [None] * N
    f_dis[0] = 0
    dfs(0, 0, conn, f_dis)

    s_dis = [None] * N
    s_dis[N - 1] = 0
    dfs(N - 1, 0, conn, s_dis)

    cnt = 0
    for i in range(N):
        if f_dis[i] <= s_dis[i]:
            cnt += 1

    if cnt > (N - cnt):
        ret = 'Fennec'
    else:
        ret = 'Snuke'
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N-1)  # type: "List[int]" 
    b = [int()] * (N-1)  # type: "List[int]" 
    for i in range(N-1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)

if __name__ == '__main__':
    main()
