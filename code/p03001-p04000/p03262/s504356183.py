import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class Gcd:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def ngcd(self, A):
        res = A[0]
        for i in range(len(A)):
            if res != 1:
                res = gcd(A[i], res)
        return res

    def lcm(self, a, b):
        return a * b // gcd(a, b)

    def nlcm(self, A):
        res = A[0]
        for i in range(len(A)):
            res = lcm(res, A[i])
        return res


def resolve():
    n, x = map(int, input().split())
    X = sorted(list(map(int, input().split())))

    dist = [0] * n
    for i in range(n):
        dist[i] = abs(x - X[i])

    g = Gcd()
    res = dist[0]
    for i in range(1, len(dist)):
        res = g.gcd(res, dist[i])
    print(res)


if __name__ == '__main__':
    resolve()
