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


N = ii()
A = il()
B = il()
S = 0
diff = []
num_i = 0
for a, b in zip(A, B):
    if a < b:
        S += b - a
        num_i += 1
    else:
        diff.append(a - b)
diff.sort(reverse=True)
if num_i == 0:
    print(0)
    exit()
c = 0
for i in range(len(diff)):
    S -= diff[i]
    c += 1
    if S < 0:
        break
else:
    print(-1)
    exit()
print(num_i + c)
