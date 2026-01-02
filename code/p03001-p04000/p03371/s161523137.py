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

def main():
    ans = 0
    a,b,c,x,y = getList()


    if x > y:
        ans1 = (c * 2 * y + a * (x - y))
    else:
        ans1 = (c * 2 * x + b * (y - x))

    ans2 = (a * x + b * y)

    ans3 = c * 2 * max(x, y)

    print(min(ans1, ans2, ans3))
    return

if __name__ == "__main__":
    main()