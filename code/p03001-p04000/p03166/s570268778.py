from collections import defaultdict, deque


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M = read_ints()
    out_degree = [0]*N
    max_path = [0]*N
    G = defaultdict(list)
    for _ in range(M):
        x, y = read_ints()
        x -= 1
        y -= 1
        out_degree[x] += 1
        G[y].append(x)
    Q = [i for i, degree in enumerate(out_degree) if degree == 0]
    while len(Q):
        node = Q.pop()
        while len(G[node]):
            parent = G[node].pop()
            out_degree[parent] -= 1
            max_path[parent] = max(max_path[parent], max_path[node]+1)
            if out_degree[parent] == 0:
                Q.append(parent)
    return max(max_path)


if __name__ == '__main__':
    print(solve())
