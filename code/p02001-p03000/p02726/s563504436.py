import collections


def bfs(i, path, dist, N):
    moves = 0

    pp = []
    pp = path[i]

    reached = [False for _ in range(N)]
    dist[i] = 0
    reached[i] = True
    for j in range(N + 1):
        moves += 1
        next_pp = []
        for i in pp:
            if reached[i]:
                continue
            else:
                reached[i] = True
                dist[i] = moves
                for p in path[i]:
                    next_pp.append(p)

        pp = next_pp


def flatten(nested_list):
    return [e for inner_list in nested_list for e in inner_list]


def main():
    N, X, Y = map(int, input().split())

    path = [[] for _ in range(N)]

    for i in range(N - 1):
        path[i].append(i + 1)
        path[i + 1].append(i)

    path[X - 1].append(Y - 1)
    path[Y - 1].append(X - 1)

    dist = [N for _ in range(N)]

    D_list = []

    for i in range(N):
        dist[i] = 0
        bfs(i, path, dist, N)
        D_list.append(dist)
        dist = [N for _ in range(N)]

    D = flatten(D_list)
    dic = collections.Counter(D)

    for i in range(1, N):
        print(dic[i] // 2)


main()
