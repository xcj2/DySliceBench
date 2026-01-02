import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N, X = map(int, input().split())
    a = [0]*N
    p = [0]*N
    a[0] = 1
    p[0] = 1
    for i in range(1, N):
        a[i] = a[i-1]*2+3
        p[i] = p[i-1]*2+1

    def rec(N, X):
        if X == 1 and N == 0:
            return 1
        elif X == 1 and N != 0:
            return 0
        elif 2 <= X <= 1+a[N-1]:
            return rec(N-1, X-1)
        elif X == 2+a[N-1]:
            return p[N-1]+1
        elif 3+a[N-1] <= X <= 2+a[N-1]*2:
            return p[N-1]+rec(N-1, X-a[N-1]-2)+1
        else:
            return p[N-1]*2+1
    print(rec(N, X))


resolve()