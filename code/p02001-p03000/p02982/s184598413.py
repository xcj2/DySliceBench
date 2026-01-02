from sys import stdin

def bisearch(f, n):
    l = 0
    r = n
    fl = f(l)
    fr = f(r)
    while l <= r:
        m = (l + r) // 2
        fm = f(m)
        if fm == n:
            return True
        elif fm > n:
            r = m - 1
            fr = f(r)
        else:
            l = m + 1
            fl = f(l)
    return False

def is_sqrt(n):
    return bisearch(lambda m: m * m, n)

def main():
    N, D = map(int, input().split())
    X = [tuple(map(int, input().split())) for _ in [0] * N]

    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            n = 0
            for d in range(D):
                n += (X[i][d] - X[j][d]) ** 2
            ans += is_sqrt(n)
    print(ans)

input = lambda: stdin.readline()
main()
