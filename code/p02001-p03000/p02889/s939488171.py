import sys

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))


def warshall_floyd(d, n):

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

def main():
    n, m, l = LI()
    mem = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(m):
        a, b, c = LI()
        mem[a-1][b-1] = c
        mem[b-1][a-1] = c
    for i in range(n):
        mem[i][i] = 0
    mem = warshall_floyd(mem, n)
    new_mem = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mem[i][j] <= l:
                new_mem[i][j] = 1

    new_mem = warshall_floyd(new_mem, n)
    q = II()
    for i in range(q):
        s, t = LI()
        print(new_mem[s-1][t-1] - 1 if new_mem[s-1][t-1] < INF else -1)


if __name__ == '__main__':
    main()