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

def cone(n):
    if n == 0:
        return 0
    else:
        return n

def ctwo(n):
    if n <= 1:
        return 0
    else:
        return(n * (n-1)) // 2

def ketaall(keta, m):
    if m == 0:
        return 1
    if m == 1:
        return keta * 9
    else:
        return ctwo(keta) * 81


def main():
    n = getN()
    n = str(n)
    keta = len(n) - 1
    m = getN()
    if m == 1:
        res = 0
        print(int(int(n[0]) + 9 * keta))
        return

    res = (int(n[0]) - 1)*  ketaall(keta, m -1)
    # print(res, n[0], n, keta)
    for k in range(int(keta)):
        res += 9 * ketaall(k, m-1)
        # print(res)

    m -= 1
    # print("====================")
    for s in n[1:]:
        if s == "0":
            pass
        else:
            res += ketaall(keta - 1, m)
            # print(res)
            res += (int(s) - 1) * ketaall(keta-1, m-1)
            # print(res)
            m -= 1

        keta -= 1
        # print(res, m)
        if m == 0:
            res += 1
            break

    print(res)


if __name__ == '__main__':
    main()

"""
9999
3

2916
"""