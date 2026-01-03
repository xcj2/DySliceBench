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
    N = int(input().strip())
    C = [10 ** 5] * 26
    for _ in range(N):
        tmp = [0] * 26
        S = input().strip()
        for s in S:
            tmp[ord(s) - ord("a")] += 1

        for i in range(26):
            C[i] = min(C[i], tmp[i])

    res = ""
    for i, c in enumerate(C):
        if c == 0:
            continue
        res += chr(i + ord("a")) * c
    print(res)


if __name__ == "__main__":
    main()

