import sys
input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import heapq
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**15


def main():
    n = getN()
    ans = 0
    runruns = [[str(i) for i in range(10)]]
    for digit in range(9):
        tmp = []
        for i in range(10):
            stri = str(i)
            for run in runruns[-1]:
                if abs(i - int(run[0])) <= 1:
                    tmp.append(stri + run)

        tmp.sort()
        runruns.append(tmp)
    runruns = [[r for r in run if r[0] != "0"] for run in runruns]
    # print(sum([len(run) for run in runruns]))
    # print(runruns[-2])
    ans = []
    for run in runruns:
        ans = ans + run

    print(ans[n-1])
    # print(ans)
if __name__ == '__main__':
    main()
