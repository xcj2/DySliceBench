import math
INF, MOD = float("inf"), 1e9 + 7
MAX, MIN = -INF, INF
dx1, dy1, dx2, dy2 = [-1, 0, 1, 0], [0, -1, 0, 1], [-1, 0, 1, -1, 1, -1, 0, 1], [-1, -1, -1, 0, 0, 1, 1, 1]

def get_int():
    return int(input())

def get_int_list():
    return list(map(int, input().split()))

def mins(x, y):
    x = min(x, y)

def maxs(x, y):
    x = max(x, y)

while(True):
    try:
        cnt = [0] * 5
        for i in range(3):
            a, b = get_int_list()
            cnt[a] += 1
            cnt[b] += 1
        if cnt.count(2) == 2:
            print("YES")
        else:
            print("NO")
    except EOFError:
        exit()
