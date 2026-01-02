import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def is_consistent(cx, cy, X, Y, H, N):
    h_proposal = None
    max_h = math.inf
    for i in range(N):
        if H[i] > 0:
            if h_proposal is not None and h_proposal != H[i]+abs(X[i]-cx)+abs(Y[i]-cy):
                return None
            h_proposal = H[i]+abs(X[i]-cx)+abs(Y[i]-cy)
        else:
            max_h = min(max_h, abs(X[i]-cx)+abs(Y[i]-cy))
    if h_proposal is not None and h_proposal <= max_h:
        return cx, cy, h_proposal

def solve():
    N = read_int()
    X, Y, H = [], [], []
    for _ in range(N):
        x, y, h = read_ints()
        X.append(x)
        Y.append(y)
        H.append(h)
    # h == max(H-abs(x-cx)-abs(y-cy), 0)
    for cx in range(101):
        for cy in range(101):
            answer = is_consistent(cx, cy, X, Y, H, N)
            if answer is not None:
                return answer


if __name__ == '__main__':
    print(*solve())
