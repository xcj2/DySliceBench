

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    tree = [[] for  _ in range(N)]
    abs = []
    for _ in range(N-1):
        a, b = read_ints()
        a -= 1
        b -= 1
        abs.append((a, b))
        tree[a].append(b)
    Q = [(0, -1)]
    colors = {}
    color_count = 0
    while Q:
        node, color = Q.pop()
        c = 1
        for child in tree[node]:
            if color == c:
                c += 1
            colors[(node, child)] = c
            Q.append((child, c))
            color_count = max(color_count, c)
            c += 1
    print(color_count)
    for ab in abs:
        print(colors[ab])


if __name__ == '__main__':
    solve()
