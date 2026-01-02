import sys

sys.setrecursionlimit(200000)


def input():
    return sys.stdin.readline()[:-1]


def ii(t: type = int):
    return t(input())


def il(t: type = int):
    return list(map(t, input().split()))


def imi(N: int, t: type = int):
    return [ii(t) for _ in range(N)]


def iml(N: int, t: type = int):

    return [il(t) for _ in range(N)]


def solve():
    N = ii()
    # 時刻ｔにx, yを訪れる
    # t+1 で (x+1, y), (x-1, y), (x, y+1), (x, y-1)に移動
    T = [0] * (N + 1)
    X = [0] * (N + 1)
    Y = [0] * (N + 1)
    for n in range(N):
        t = il()
        T[n + 1] = t[0]
        X[n + 1] = t[1]
        Y[n + 1] = t[2]
    for i in range(N):
        dt = T[i + 1] - T[i]
        dst = abs(X[i + 1] - X[i]) + abs(Y[i + 1] - Y[i])
        if dt < dst or dt % 2 != dst % 2:
            return "No"
    return "Yes"


if __name__ == "__main__":
    print(solve())
