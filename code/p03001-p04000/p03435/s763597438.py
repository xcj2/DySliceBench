import sys


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


C = iml(3)
b = [C[0][0], C[0][1], C[0][2]]
a = [0, C[1][0] - C[0][0], C[2][0] - C[0][0]]
for i in range(1, 3):
    for j in range(1, 3):
        if a[i] + b[j] != C[i][j]:
            print("No")
            exit()
print("Yes")
