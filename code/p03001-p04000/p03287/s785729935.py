import sys
input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import heapq
import bisect
import copy
import math
from collections import defaultdict

def warshall_floyd(d, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i * N +j] = min(d[i * N +j], d[i * N + k] + d[k * N + j])
    return d

MOD = 10**9 + 7

def main():
    n,m = getlist()
    anums = getlist()

    accsum = [0]
    tmp = 0

    for anum in anums:
        tmp += anum
        tmp %= m
        accsum.append(tmp)

    cnt = defaultdict(int)

    for acc in accsum:
        cnt[acc] += 1

    res = 0

    for cn in cnt.values():
        res += (cn * (cn-1) ) // 2

    print(res)
    # print(cont)

if __name__ == '__main__':
    main()

