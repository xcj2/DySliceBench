


def update(tree, index, value):
    while index < len(tree):
        tree[index] = max(tree[index], value)
        index += index & -index


def read(tree, index):
    value = 0
    while index > 0:
        value = max(value, tree[index])
        index -= index & -index
    return value


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    h = read_ints()
    a = read_ints()
    tree = [0]*(N+1)
    max_beauty = 0
    for i in range(N):
        beauty = read(tree, h[i])+a[i]
        update(tree, h[i], beauty)
        max_beauty = max(max_beauty, beauty)
    return max_beauty


if __name__ == '__main__':
    print(solve())
