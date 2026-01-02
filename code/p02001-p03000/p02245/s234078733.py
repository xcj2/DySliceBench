from collections import deque
N = 3
def g(i, j, a):
    if i > j:
        i, j = j, i
    return a[:i] + a[j] + a[i + 1:j] + a[i] + a[j + 1:]
goal = "123456780"
def solve():
    m = {8:{7, 5}, 7:{8, 6, 4}, 6:{7, 3}, 5:{8, 4, 2}, 4:{7, 5, 3, 1}, 3:{6, 4, 0}, 2:{5, 1}, 1:{4, 2, 0}, 0:{3, 1}}
    MAP = "".join(input().replace(" ", "") for _ in range(N))
    if MAP == goal:
        return 0
    start = MAP.find("0")
    dp = deque([(0, MAP, start, 1), (0, goal, 8, 0)])
    TABLE = {MAP:(1, 0), goal:(0, 0)}
    while dp:
        cnt, M, yx, flg = dp.popleft()
        cnt += 1
        for nyx in m[yx]:
            CM = g(yx, nyx, M)
            if CM in TABLE:
                if TABLE[CM][0] != flg:
                    return TABLE[CM][1] + cnt
                continue
            TABLE[CM] = (flg, cnt)
            dp.append((cnt, CM, nyx, flg))
def MAIN():
    print(solve())
MAIN()

