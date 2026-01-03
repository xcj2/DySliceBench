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
    line = []
    for i in range(n):
        line.append((getN(), "P"))
    for i in range(n):
        line.append((getN(), "C"))

    line.sort()
    pc = 0
    cn = 0
    ans = 1
    # print(line)
    for point in line:
        pt, st = point
        if st == "P":
            if pc == 0 and cn != 0:
                ans *= cn
                ans %= MOD
                cn -= 1
            else:
                pc += 1

        else:
            if cn == 0 and pc != 0:
                ans *= pc
                ans %= MOD
                pc-=1
            else:
                cn += 1

    print(ans)



if __name__ == '__main__':
    main()

"""
9999
3

2916
"""