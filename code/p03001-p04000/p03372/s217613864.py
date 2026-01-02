import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
import bisect
from logging import getLogger, StreamHandler, DEBUG, WARNING
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
handler.setLevel(WARNING)
logger.setLevel(WARNING)
logger.addHandler(handler)
logger.propagate = False


# class SegTree():
#     def __init__(self, n):
#         self.value = [0 for i in range(n*2)]

# MOD = 10 ** 9 + 7

# def getinvmod(n):
#     return [pow(i, MOD-2, MOD) for i in range(n+1)]

def main():
    n, m = getList()
    sushis = []
    for i in range(n):
        sushis.append(getList())

    tmp = 0
    acc = [(0, 0)]
    acc2 = [0]
    acc2idx = [0]

    for sushi in sushis:
        tmp += sushi[1]
        if tmp - sushi[0] > acc[-1][1]:
            acc.append((sushi[0], tmp - sushi[0]))
        if tmp - 2 * sushi[0] > acc2[-1]:
            acc2.append(tmp - sushi[0] * 2)
            acc2idx.append(sushi[0])

    tmp = 0
    racc = [(0, 0)]
    racc2 = [0]
    racc2idx = [0]

    for sushi in sushis[::-1]:
        tmp += sushi[1]
        dist = m - sushi[0]
        if tmp - dist > racc[-1][1]:
            racc.append((sushi[0], tmp - dist))
        if tmp - 2 * dist > racc2[-1]:
            racc2.append(tmp - 2 * dist)
            racc2idx.append(dist)


    ans = 0
    for asu in acc:
        tmp = asu[1]
        idx = bisect.bisect_left(racc2idx, m - asu[0])
        tmp += racc2[idx - 1]
        if tmp > ans:
            ans = tmp
            logger.info(asu, tmp, idx)

    for asu in racc:
        tmp = asu[1]
        idx = bisect.bisect_left(acc2idx, asu[0])
        tmp += acc2[idx - 1]
        if tmp > ans:
            ans = tmp
            logger.info(asu, tmp)

    print(ans)
    logger.info(acc, acc2)
    logger.info(racc, racc2, racc2idx)

    return
if __name__ == "__main__":
    main()