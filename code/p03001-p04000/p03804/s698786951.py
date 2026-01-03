import sys

# sys.stdin = open('b1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


N, M = read_int_list()
A = [read_str() for i in range(N)]
B = [read_str() for j in range(M)]


def g(n, m, a, b, i, j):
    for k in range(m):
        for l in range(m):
            if a[i + k][j + l] != b[k][l]:
                return False
    return True


def f(N, M, A, B):
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            if g(N, M, A, B, i, j):
                return 'Yes'
    return 'No'

print(f(N, M, A, B))
