import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
import bisect
from logging import getLogger, StreamHandler, DEBUG, WARNING
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
# handler.setLevel(WARNING)
# logger.setLevel(WARNING)
logger.addHandler(handler)



# class SegTree():
#     def __init__(self, n):
#         self.value = [0 for i in range(n*2)]

# MOD = 10 ** 9 + 7

# def getinvmod(n):
#     return [pow(i, MOD-2, MOD) for i in range(n+1)]

def judge(a1, a2, a3, nums):
    b1 = nums[0][0] - a1
    b2 = nums[0][1] - a1
    b3 = nums[0][2] - a1
    if a2 + b1 == nums[1][0] and a2 + b2 == nums[1][1] and a2 + b3 == nums[1][2]:
        if a3 + b1 == nums[2][0] and a3 + b2 == nums[2][1] and a3 + b3 == nums[2][2]:
            return True

    return False

def main():
    nums = [getList() for _ in range(3)]
    for a1 in range(101):
        for a2 in range(101):
            for a3 in range(101):
                if judge(a1, a2, a3, nums):
                    print("Yes")
                    return

    print("No")

if __name__ == "__main__":
    main()