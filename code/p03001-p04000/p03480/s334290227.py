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
def main():
    s = input().strip()
    n = len(s)
    tmp = s[0]
    ans = 0
    for i , c in enumerate(s):
        if tmp != c:
            if i > ans:
                ans = i

        if i >= (n) // 2:
            break
        tmp = c


    tmp = s[-1]
    for i, c in enumerate(s[::-1]):
        if tmp != c:
            if i > ans:
                ans = i

        if i >= (n) // 2:
            break
        tmp = c

    print(n - ans)

    # print("No")

if __name__ == "__main__":
    main()