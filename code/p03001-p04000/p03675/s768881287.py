import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
from collections import deque

class SegTree():
    def __init__(self, n):
        self.value = [0 for i in range(n*2)]



def main():
    n = getN()
    nums = getList()
    d = deque()
    for i, num in enumerate(nums):
        if i % 2 != n % 2:
            d.appendleft(num)
        else:
            d.append(num)


    print(*d)

if __name__ == "__main__":
    main()