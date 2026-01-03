# coding: utf-8
from collections import defaultdict

INF = 10 ** 20
MOD = 10 ** 9 + 7


def II(): return int(input())
def ILI(): return list(map(int, input().split()))


def read():
    N, M = ILI()
    edges = defaultdict(list)
    for __ in range(M):
        a, b = ILI()
        edges[a].append(b)
        edges[b].append(a)
    return N, M, edges


def solve(N, M, edges):
    s_from_1 = set(edges[1])
    s_from_n = set(edges[N])
    set_and = s_from_1 & s_from_n
    ans = ""
    if len(set_and) == 0:
        ans = "IMPOSSIBLE"
    else:
        ans = "POSSIBLE"
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
