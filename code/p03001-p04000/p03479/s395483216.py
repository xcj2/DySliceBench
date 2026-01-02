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
    x, y = getList()
    ans = 0
    while(True):
        if x <= y:
            ans += 1
            x *= 2
        else:
            break

    print(ans)
if __name__ == "__main__":
    main()