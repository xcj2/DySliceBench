import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import heapq
import bisect
import copy
# import math
def warshall_floyd(d, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i * N +j] = min(d[i * N +j], d[i * N + k] + d[k * N + j])
    return d

MOD = 10**9 + 7

def main():
    t1, t2 = getlist()
    a1, a2 = getlist()
    b1, b2 = getlist()
    if (a1 > b1 and a2 > b2) or (a1 < b1 and a2 < b2):
        print(0)
        return

    if t1 * a1 + t2 * a2 == b1 * t1 + b2 * t2:
        print("infinity")
        return

    if t1 * a1 + t2 * a2 < b1 * t1 + b2 * t2:
        # 多く走る方がa
        a1, a2, b1, b2 = b1, b2, a1, a2


    if a1 < b1:
        gap = (b1 - a1) * t1
        totalgap = (t1 * a1 + t2 * a2) - (b1 * t1 + b2 * t2)
        # print(gap, totalgap)
        ans = 1 + (gap // totalgap) * 2 - (gap % totalgap == 0)
        print(ans)

    else:
        print(0)


if __name__ == '__main__':
    main()

