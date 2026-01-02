from itertools import permutations as perm
from copy import deepcopy as copy


def inpl():
    return tuple(map(int, input().split()))


def dfs(XY, flag):
    # print(len(XY), XY, sum(f.count(True) for f in flag))
    if len(XY) == 8:
        # print("here")
        return XY

    for i in range(8*8):
        x = i // 8
        y = i % 8
        if flag[x][y] is False:
            continue
        f, new_f = toFalse(x, y, flag, XY)
        if f is False:
            continue
        tmp = copy(XY)
        tmp.add((x, y))
        # print(tmp)
        ret = dfs(tmp, new_f)
        if ret is None:
            continue
        else:
            return ret
    return None


def toFalse(x, y, f, XY):
    flag = copy(f)
    ddd = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
    for i in range(8):
        # print(x, y, i, flag)
        if (i, y) in XY or (x, i) in XY:
            return False, flag
        else:
            flag[i][y] = False
            flag[x][i] = False

        if i == 0:
            continue
        for dx, dy in ddd:
            if not(0 <= x + i*dx < 8 and 0 <= y + i*dy < 8):
                continue
            elif (x+i*dx, y+i*dy) in XY:
                return False, flag
            else:
                flag[x+i*dx][y+i*dy] = False
    return True, flag


N = int(input())
XY = [inpl() for _ in range(N)]


flag = [[True for _ in range(8)] for i in range(8)]
# print(flag)
for x, y in XY:
    f, flag = toFalse(x, y, flag, set())

ans = dfs(set(XY), flag)

# print(ans)
chess = [["."]*8 for i in range(8)]
for x, y in ans:
    chess[x][y] = "Q"
for c in chess:
    print("".join(c))

