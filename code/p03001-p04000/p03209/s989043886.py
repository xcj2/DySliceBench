def L(N):
    if N == 0:
        return 1
    return 3 + 2 * L(N-1)
def P(N):
    if N == 0:
        return 1
    return 1 + 2 * P(N-1)

def A(N,X):
    res = 0
    if N == 0:
        return 1
    if X == 1:
        return 0
    if 1 < X <= L(N-1) + 1:
        res = A(N-1,X-1)
    elif L(N-1) + 2 == X:
        res = 1 + P(N-1)
    elif L(N-1) + 2 < X <= 2 * L(N-1) + 2:
        res = 1 + P(N-1) + A(N-1,X-(2+L(N-1)))
    elif 2 * L(N-1) + 3 == X:
        res = 1 + 2 * P(N-1)
    return res

def main():
    N, X = map(int, input().split())
    print(A(N,X))


if __name__ == "__main__":
    main()