import sys
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N, X = mi()
    a, p = [1], [1]
    for i in range(N):
        a.append(a[i]*2+3)
        p.append(p[i]*2+1)

    def f(N, X):
        if N == 0:
            return 0 if X <= 0 else 1

        if X <= 1 + a[N-1]:
            return f(N-1, X-1)
        else:
            return p[N-1]+1+f(N-1, X-2-a[N-1])

    print(f(N, X))

if __name__ == '__main__':
    main()
