import sys


def sum(tree, i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s


def add(tree, size,  i, x):
    while i <= size:
        tree[i] += x
        i += i & -i


def range_sum(tree, l, r):
    return sum(tree, r) - sum(tree, l)


def main():
    n, q = map(int, sys.stdin.buffer.readline().split())

    bit = [0] + list(map(int, sys.stdin.buffer.readline().split()))
    for i in range(1, n+1):
        if i + (i & -i) < n + 1:
            bit[i + (i & -i)] += bit[i]

    for y in sys.stdin.buffer.readlines():
        q, p, x = map(int, y.split())
        if q:
            print(range_sum(bit, p, x))
        else:
            add(bit,n, p+1, x)


if __name__ == "__main__":
    main()
