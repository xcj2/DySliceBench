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

def main():
    n = getN()
    lucky = str(input().strip())
    one = [0 for i in range(10)]
    two = [0 for i in range(100)]
    thr = [0 for i in range(1000)]
    # print(lucky)
    for s in lucky:
        # print(s)
        for tin, tis in enumerate(two):
            if tis == 1:
                thr[int(str(tin) + s)] = 1

        for oin, ois in enumerate(one):
            if ois == 1:
                # print(int(str(tin) + s))
                two[int(str(oin) + s)] = 1
        one[int(s)] = 1


    print(sum(thr))
if __name__ == '__main__':
    main()

