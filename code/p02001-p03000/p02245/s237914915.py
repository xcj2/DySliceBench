from collections import deque
N = 3
m = {8: {7, 5}, 7: {8, 6, 4}, 6: {7, 3}, 5: {8, 4, 2}, 4: {7, 5, 3, 1}, 3: {6, 4, 0}, 2: {5, 1}, 1: {4, 2, 0},
     0: {3, 1}}
goal = 123456780
def g(i, j, a):
    t = a // (10 ** j) % 10
    return a - t * (10 ** j) + t * (10 ** i)
def solve():
    MAP = "".join(input().replace(" ", "") for _ in range(N))
    start = 8 - MAP.find("0")
    MAP = int(MAP)
    if MAP == goal:
        return 0
    dp = deque([(0, start, MAP)])
    LOG = {MAP}
    while dp:
        cnt, yx, M = dp.popleft()
        if M == goal:
            return cnt
        cnt += 1
        for nyx in m[yx]:
            CM = g(yx, nyx, M)
            if not CM in LOG:
                dp.append((cnt, nyx, CM))
                LOG.add(CM)
def MAIN():
    print(solve())
MAIN()

