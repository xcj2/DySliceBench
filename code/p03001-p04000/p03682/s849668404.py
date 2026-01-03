#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, x: "List[int]", y: "List[int]"):
    tmp = []
    for i in range(N):
        tmp.append([i, x[i], y[i]])
    tmp.sort(key=lambda x: x[1])
    dis = []
    for i in range(N - 1):
        dis.append([abs(tmp[i + 1][1] - tmp[i][1]), tmp[i][0], tmp[i + 1][0]])

    tmp.sort(key=lambda x: x[2])
    for i in range(N - 1):
        dis.append([abs(tmp[i + 1][2] - tmp[i][2]), tmp[i][0], tmp[i + 1][0]])

    par = list(range(N))
    def find_root(x):
        if par[x] != x:
            par[x] = find_root(par[x])
        return par[x]
    def union(a, b):
        a_root = find_root(a)
        b_root = find_root(b)
        par[a_root] = b_root
        return

    dis.sort(key=lambda x: x[0])
    ret = 0
    for d in dis:
        a = d[1]
        b = d[2]
        if find_root(a) != find_root(b):
            ret += d[0]
            union(a, b)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]" 
    y = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)

if __name__ == '__main__':
    main()
