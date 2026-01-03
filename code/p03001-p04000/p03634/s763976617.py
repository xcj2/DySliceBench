from collections import defaultdict


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    G = defaultdict(list)
    for _ in range(N-1):
        a, b, c = read_ints()
        G[a].append((b, c))
        G[b].append((a, c))
    Q, K = read_ints()

    dist = [0]*(N+1)
    stack = [(None, 0, K)]
    while stack:
        parent, base_d, node = stack.pop()
        for child, d in G[node]:
            if child != parent:
                dist[child] = base_d+d
                stack.append((node, base_d+d, child))

    for _ in range(Q):
        x, y = read_ints()
        print(dist[x]+dist[y])


if __name__ == '__main__':
    solve()
