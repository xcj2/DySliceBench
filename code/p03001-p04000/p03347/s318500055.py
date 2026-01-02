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
    A = [int(input()) for _ in range(N)]
    if A[0] != 0:
        print(-1)
        return
    
    for i in range(N - 1):
        if A[i + 1] - A[i] > 1:
            print(-1)
            return
    
    res = 0
    c = 0
    for a in A[::-1]:
        if c < a:
            res += a
            c = a
        c -= 1
    print(res)


if __name__ == "__main__":
    main()

