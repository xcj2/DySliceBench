# -*- coding: utf-8 -*-

# sys.setrecursionlimit(100000)
INF = 2**62-1

def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)

def slv(N, M, Q, ABCD):

    def dfs(a, n):
        r = 0
        if n == N:
            t = 0
            for abcd in ABCD:
                A, B, C, D = abcd
                if a[B] - a[A] == C:
                    t += D
            return t
        b = a[-1]
        for c in range(b, M+1):
            a.append(c)
            r = max(r, dfs(a, n+1))
            a.pop()
        return r
    return dfs([1], 0)


def main():
    N, M, Q = read_int_n()
    ABCD = [read_int_n() for _ in range(Q)]
    print(slv(N, M, Q, ABCD))


if __name__ == '__main__':
    main()
