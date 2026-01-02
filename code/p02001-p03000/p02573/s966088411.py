def main():
    n, m, *ab, = map(int, open(0).read().split())
    p = [-1] * (n + 1)

    def find(x):
        while p[x] > 0:
            x = p[x]
        return x

    def union(i, j):
        pi, pj = find(i), find(j)
        if pi == pj:
            return
        if p[pi] < p[pj]:
            pi, pj = pj, pi
            i, j = j, i
        p[pi] += p[pj]
        p[pj] = pi
        reconnect(j, pi)

    def reconnect(i, j):
        while p[i] > 0:
            k = p[i]
            p[i] = j
            i = k

    for i, j in zip(ab[::2], ab[1::2]):
        union(i, j)

    print(-min(p))


if __name__ == '__main__':
    main()
