import sys

input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def func(N, mod):
    F = [1]
    for i in range(1, N + 1):
        F.append(F[-1] * i % mod)
    return F


INV = {}


def inv(a, mod):
    if a in INV:
        return INV[a]
    r = pow(a, mod - 2, mod)
    INV[a] = r
    return r


def C(F, a, b, mod):
    return F[a] * inv(F[b], mod) * inv(F[a - b], mod) % mod


def main():
    import bisect

    N, W = read_values()
    I = [tuple(read_values()) for _ in range(N)]

    init_w = I[0][0]
    D = {i: [] for i in range(4)}
    S = {i: [0] for i in range(4)}
    for w, v in I:
        bisect.insort(D[w - init_w], -v)

    for i, d in D.items():
        for v in d:
            S[i].append(v + S[i][-1])

    res = 0
    for t0 in range(len(D[0]) + 1):
        for t1 in range(len(D[1]) + 1):
            for t2 in range(len(D[2]) + 1):
                for t3 in range(len(D[3]) + 1):
                    if (t0 + t1 + t2 + t3) * init_w + t1 + 2 * t2 + 3 * t3 > W:
                        continue

                    res = min(res, S[0][t0] + S[1][t1] + S[2][t2] + S[3][t3])
    print(-res)


if __name__ == "__main__":
    main()

