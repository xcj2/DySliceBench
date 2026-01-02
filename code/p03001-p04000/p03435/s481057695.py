import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import bisect
import heapq
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**15

def main():
    a,b,c = getlist()
    s12 = b - a
    s13 = c - a
    s23 = c - b
    for i in range(2):
        d,e,f = getlist()
        # print(d,e,f)
        # print(s12,s23,s13)
        if e-d != s12:
            # print(e-d)
            print("No")
            return
        if f-d != s13:
            print("No")
            return
        if f-e != s23:
            print("No")
            return

    print("Yes")
    return

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""