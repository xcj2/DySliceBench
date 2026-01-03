import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def max_diff(*A):
    return max(A)-min(A)


def _solve(H, W):
    # W is set
    min_diff = math.inf
    for h in range(1, H):
        min_diff = min(min_diff, max_diff(W*h, (W//2)*(H-h), (W-W//2)*(H-h)),
                                 max_diff(W*h, ((H-h)//2)*W, (H-h-(H-h)//2)*W))
    return min_diff


def solve():
    H, W = read_ints()
    return min(_solve(H, W), _solve(W, H))


if __name__ == '__main__':
    print(solve())
