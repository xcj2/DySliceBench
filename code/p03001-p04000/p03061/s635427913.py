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
import fractions
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**15

def getyaku(n):
    res = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)

    return(sorted(list(set(res))))

def judge(cand, nums):
    w = 0
    for num in nums:
        if num % cand !=0:
            if w == 1:
                return False
            else:
                w += 1

    return True

def main():
    n = getN()
    nums = getlist()

    ans = 0
    cands = getyaku(nums[0])

    for cand in cands:
        if judge(cand, nums):
            if ans < cand:
                ans = cand
    cands = getyaku(nums[1])

    for cand in cands:
        if judge(cand, nums):
            if ans < cand:
                ans = cand

    print(ans)
    return

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""