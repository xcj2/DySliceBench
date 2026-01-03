import sys
# input = sys.stdin.buffer.readline
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
    # n, m = getlist()
    # nums = getlist()
    s = input().strip()
    dic = dict(Counter(s))
    for i in range(n-1):
        s = input().strip()
        cnt = dict(Counter(s))
        for k in dic.keys():
            if k not in cnt:
                dic[k] = 0
        for k,v in cnt.items():
            if k in dic:
                dic[k] = min(dic[k], v)

    # print(sorted(dic.items()))
    ans = ""

    for k,v in sorted(dic.items(), key=lambda x: x[0]):
        # print(k, v)
        for _ in range(v):
            ans += k

    print(ans)

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""