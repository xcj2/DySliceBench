import sys

sys.setrecursionlimit(10 ** 7)

debug = True
debug = False


def dprint(*objects):
    if debug == True:
        print(*objects)



def solve():
    N, D = map(int, input().split())
    x_list = []
    for i in range(N):
        x_list.append(list(map(int, input().split())))

    def dist(x, y):
        d = 0
        for xi, yi in zip(x, y):
            d += (xi-yi)**2
        return d

    import math
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            d = math.sqrt(dist(x_list[i], x_list[j]))

            if d - int(d) == 0:
                cnt += 1

    print(cnt)
solve()