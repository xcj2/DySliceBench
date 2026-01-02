import sys
from itertools import islice, repeat


def _resolve(costs, k):
    sum_ = sum(costs)
    v = 0
    if k >= len(costs):
        if sum_ > 0:
            x = k // len(costs) - 1
            v = x * sum_
            k -= x * len(costs)
        else:
            k = len(costs)

    points = [v] * (len(costs) * (k + 1))
    for i in range(k):
        for n in range(len(costs)):
            points[(i + 1) * len(costs) + n] = points[i * len(costs) + n] + costs[(i + n) % len(costs)]
    
    ans = max(points)
    if ans == 0:
        y = max(costs)
        if y < 0:
            ans = y
    return ans


def resolve(in_):
    N, K = map(int, next(in_).split())
    P = [0] + list(map(int, next(in_).split()))
    C = [0] + list(map(int, next(in_).split()))

    graphs = []
    p = set(P[1:])
    while p:
        index = p.pop()
        graph = [C[index]]
        index = P[index]
        while index in p:
            graph.append(C[index])
            p.remove(index)
            index = P[index]
        graphs.append(graph)

    ans = max(map(_resolve, graphs, repeat(K)))
    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
