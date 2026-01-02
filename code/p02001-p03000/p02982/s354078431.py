import math


def read():
    N, D = list(map(int, input().strip().split()))
    X = [[] for _ in range(N)]
    for i in range(N):
        X[i] = list(map(int, input().strip().split()))
    return N, D, X


def is_close(x, eps):
    e = math.fmod(x, 1)
    return e < eps


def solve(N, D, X):
    count = 0
    for i in range(N):
        for j in range(N):
            if i < j:
                distance = 0
                for y, z in zip(X[i], X[j]):
                    distance += ((y - z) ** 2)
                if is_close(math.sqrt(distance), 1e-7):
                    count += 1
    return count


if __name__ == '__main__':
    inputs = read()
    print("%d" % solve(*inputs))
