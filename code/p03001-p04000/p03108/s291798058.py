import sys
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def root(P, C, a):
    if P[a] == a:
        return a
    r = root(P, C, P[a])
    P[a] = r
    C[a] = C[r]
    return r


def main():
    N, M = read_values()
    V = [read_list() for _ in range(M)]
    P = [i for i in range(N)]
    C = [1] * N
    res = [N * (N - 1) // 2] * M
    total = 0
    for i in range(M - 2, -1, -1):
        a, b = V[i + 1]
        a -= 1
        b -= 1

        ra = root(P, C, a)
        rb = root(P, C, b)
        if ra == rb:
            res[i] -= total
            continue

        P[ra] = rb
        total += C[ra] * C[rb]
        C[ra] += C[rb]
        C[rb] = C[ra]
        res[i] -= total

    print("\n".join(map(str, res)))
    

if __name__ == "__main__":
    main()