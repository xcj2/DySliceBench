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
    n,m = getlist()
    nums = getlist()

    cnt = Counter(nums)
    mod = [0 for i in range(m)]
    same = [0 for i in range(m)]

    for k, v in cnt.items():
        mod[k%m] += v
        same[k%m] += v // 2

    ans = mod[0] // 2
    for i in range(1, int((m+2) // 2)):
        if i == m / 2:
            ans += mod[i] // 2
        else:
            other = m - i
            ans += min(mod[i], mod[other])
            if mod[i] > mod[other]:
                ans += min(same[i], (mod[i] - mod[other]) // 2)
            if mod[i] < mod[other]:
                ans += min(same[other], -(mod[i] - mod[other]) // 2)

    print(ans)

    # print(same, mod)

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""