def solve(N, X):
    thickness = [1]
    pate = [1]
    for L in range(1, N + 1):
        thickness.append(thickness[-1] * 2 + 3)
        pate.append(pate[-1] * 2 + 1)

    def sub(t, X):
        middle = (thickness[t] - 1) // 2
        if t == 0:
            return 1
        if X <= 0:
            return 0
        if X < middle:
            return sub(t - 1, X - 1)
        if X == middle:
            return pate[t - 1] + 1
        return pate[t - 1] + 1 + sub(t - 1, X - middle - 1)

    return sub(N, X - 1)

def test():
    def f(N, X, expect):
        print('N={}, X={}'.format(N, X))
        print(solve(N, X), 'expect={}'.format(expect))
    f(2, 7, 4)
    f(2, 8, 4)
    f(2, 9, 5)
    f(50, 4321098765432109, 2160549382716056)

    print('-'*5)
    for i in range(1, 14): f(2, i, '')

    print('-'*5)
    for i in range(1, 6): f(1, i, '')


if __name__ == '__main__':
    N, X = map(int, input().split())
    print(solve(N, X))