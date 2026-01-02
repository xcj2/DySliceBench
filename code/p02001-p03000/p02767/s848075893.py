import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque, Counter
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
INF = 10 ** 20

def main():
    n = getN()
    nums = getList()
    mid = sum(nums) // n
    ans1 = 0
    for num in nums:
        ans1 += (num - mid) ** 2

    # print(ans1)

    ans2 = 0
    mid += 1
    for num in nums:
        ans2 += (num - mid) ** 2

    # print(ans2)
    mid -= 2
    ans3 = 0
    for num in nums:
        ans3 += (num - mid) ** 2

    print(min(ans1, ans2, ans3))

if __name__ == "__main__":
    main()

