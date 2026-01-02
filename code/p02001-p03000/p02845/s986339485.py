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
    n = getN()
    nums = getlist()
    ans = 1
    bc, bv, bb = -1, -1, -1
    for num in nums:
        tmp = 0
        added = 0
        if num == bc + 1:
            tmp += 1
            if not added:
                bc += 1
                added = 1

        if num == bv + 1:
            tmp += 1
            if not added:
                bv += 1
                added = 1

        if num == bb + 1:
            tmp += 1
            if not added:
                bb += 1
                added = 1

        ans *= tmp
        ans %= MOD
    print(ans)
if __name__ == '__main__':
    main()

