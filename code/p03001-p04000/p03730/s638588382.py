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
    A, B, C = read_values()
    # n * A = m * B + C
    for i in range(1, B + 1):
        if (i * A) % B == C:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    main()

