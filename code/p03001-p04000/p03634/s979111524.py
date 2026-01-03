# coding: utf-8
from collections import defaultdict

INF = 10 ** 20
def II(): return int(input())
def ILI(): return list(map(int, input().split()))


def read():
    N = II()
    edges = defaultdict(list)
    for __ in range(N - 1):
        a, b, c = ILI()
        edges[a - 1].append((a - 1, b - 1, c)) # from, to, weight
        edges[b - 1].append((b - 1, a - 1, c))
    Q, K = ILI()
    query = [ILI() for __ in range(Q)]
    return N, edges, Q, K, query


def solve(N, edges, Q, K, query):
    K -= 1
    weight_from_k = [None] * N
    weight_from_k[K] = 0
    used = [False] * N
    used[K] = True
    queue = edges[K]
    while len(queue) != 0:
        next_queue = []
        for fro, to, weight in queue:
            if used[to]:
                continue
            weight_from_k[to] = weight_from_k[fro] + weight
            used[to] = True
            for e in edges[to]:
                next_queue.append(e)
        queue = next_queue

    ans = []
    for x, y in query:
        ans.append(weight_from_k[x - 1] + weight_from_k[y - 1])

    ans = "\n".join(map(str, ans))
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
