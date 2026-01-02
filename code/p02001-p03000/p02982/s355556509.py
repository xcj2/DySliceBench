import sys
from math import sqrt

def solve(N, D, X):
    def dist(ys, zs):
        sum = 0
        for d in range(D):
            sum += (ys[d] - zs[d])**2
        return sqrt(sum)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            d = dist(X[i], X[j])
            if d.is_integer():
                count += 1
    print(count)


def main():
    N, D = map(int, input().split())
    X = [ []]  * N
    for y in range(N):
        X[y] = list(map(int, input().split()))
    solve(N, D, X)

if __name__ == "__main__":
    main()