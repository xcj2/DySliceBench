SHIFT = 1 << 20


def main():
    N, Q = (int(i) for i in input().split())
    C = [int(i) for i in input().split()]
    Query = []
    for j in range(Q):
        le, ri = (int(i) for i in input().split())
        Query.append(ri << 40 | le << 20 | j)
    Query.sort()

    # Query復元
    for i in range(Q):
        j = Query[i] % (SHIFT)
        Query[i] >>= 20
        le = Query[i] % (SHIFT)
        Query[i] >>= 20
        ri = Query[i]
        Query[i] = (le, ri, j)
    Query.append((-1, -1, -1))

    def sum(tree, i):
        s = 0
        while i > 0:
            s += tree[i]
            i -= i & -i
        return s

    def add(tree, i, x):
        while i <= N:
            tree[i] += x
            i += i & -i

    lastappend = [-1] * (N + 1)
    bit = [0] * (N + 1)
    idx = 0  # Queryのindex
    ans = [0]*Q

    for i, a in enumerate(C, start=1):
        if lastappend[a] != -1:
            add(bit, lastappend[a], -1)
        lastappend[a] = i
        add(bit, i, 1)
        while i == Query[idx][1]:
            (le, ri, j) = Query[idx]
            ans[j] = sum(bit, ri) - sum(bit, le-1)
            idx += 1

    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
