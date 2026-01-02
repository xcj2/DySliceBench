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


def inv(a, mod):
    return pow(a, mod - 2, mod)


def C(F, a, b, mod):
    return F[a] * inv(F[b], mod) * inv(F[a - b], mod) % mod


def main():
    N = int(input())
    R = [tuple(read_values()) for _ in range(N)]
    B = [tuple(read_values()) for _ in range(N)]
    B.sort()
    res = 0
    paired = [False] * N
    for bx, by in B:
        t = -1
        for i, (rx, ry) in enumerate(R):
            if paired[i]:
                continue

            if rx < bx and ry < by:
                if t == -1 or R[t][1] < ry:
                    t = i

        if t != -1:
            res += 1
            paired[t] = True
    print(res)


if __name__ == "__main__":
    main()

