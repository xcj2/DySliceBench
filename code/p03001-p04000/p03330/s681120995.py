def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def f(C, D, F, r):
    import collections

    L = []
    for i, f0 in enumerate(F):
        for j, c in enumerate(f0):
            if (i + j) % 3 != r:
                continue
            L.append(c - 1)
    d = collections.Counter(L)
    res = []
    for x in range(C):
        tmp = 0
        for y, v in d.items():
            tmp += D[y][x] * v
        
        res.append((x, tmp))
    
    res.sort(key=lambda l: l[1])
    return res[:3]


def main():
    N, C = read_values()
    D = [read_list() for _ in range(C)]
    F = [read_list() for _ in range(N)]

    r0 = f(C, D, F, 0)
    r1 = f(C, D, F, 1)
    r2 = f(C, D, F, 2)
    res = 10 ** 18
    for c0, v0 in r0:
        for c1, v1 in r1:
            if c0 == c1:
                continue
            for c2, v2 in r2:
                if c2 in (c0, c1):
                    continue
                res = min(res, v0 + v1 + v2)
    
    print(res)


if __name__ == "__main__":
    main()
