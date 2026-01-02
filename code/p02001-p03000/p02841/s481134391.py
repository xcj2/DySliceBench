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
    aa, ab = getlist()
    bb, bc = getlist()
    if aa == bb:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()

