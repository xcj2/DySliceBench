import bisect


def read():
    N = int(input().strip())
    A_iter = map(int, input().strip().split())
    B_iter = map(int, input().strip().split())
    return N, A_iter, B_iter


def index(a, x):
    i = bisect.bisect_left(a, x)
    return i


def solve(N, A_iter, B_iter):
    C = []
    for a, b in zip(A_iter, B_iter):
        C.append(a - b)
    C = sorted(C)
    zero_index = index(C, 0)
    few = C[:zero_index]
    many = C[zero_index:]

    few_size = len(few)
    few_sum = -sum(few)

    if few_sum == 0:
        return few_size
    for i, m in enumerate(reversed(many)):
        few_sum -= m
        if few_sum <= 0:
            return few_size + i + 1
    return -1


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
