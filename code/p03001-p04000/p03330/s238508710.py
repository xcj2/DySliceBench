#!/usr/bin/env python3
import sys

def calc_(order, d):
    ret = 0
    for i in range(3):
        target = order[i]
        ret += d[i][target]
    return ret

def calc(G, target, D):
    ret = 0
    for elm in G:
        ret += D[elm - 1][target]
    return ret

def dfs(idx, current, used, d):
    if idx == 3:
        ret = calc_(current, d)
        return ret
    ret = float('inf')
    for i, u in enumerate(used):
        if not u:
            used[i] = True
            tmp = dfs(idx + 1, current + [i], used, d)
            ret = min(ret, tmp)
            used[i] = False
    return ret

def solve(N: int, C: int, D: "List[List[int]]", c: "List[List[int]]"):
    groups = [[] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cc = c[i][j]
            groups[(i + j) % 3].append(cc)
    #print(groups)
    d = [[] for _ in range(3)]
    for i, G in enumerate(groups):
        for j in range(C):
            d[i].append(calc(G, j, D))
    ret = dfs(0, [], [False] * C, d)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = [ [ int(next(tokens)) for _ in range(C) ] for _ in range(C) ]  # type: "List[List[int]]"
    c = [ [ int(next(tokens)) for _ in range(N) ] for _ in range(N) ]  # type: "List[List[int]]"
    solve(N, C, D, c)

if __name__ == '__main__':
    main()
