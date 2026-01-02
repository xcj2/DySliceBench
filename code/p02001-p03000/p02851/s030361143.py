import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque, Counter, defaultdict
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
    n, k = getList()
    nums = getList()
    acc = [0]
    tmp = 0
    for num in nums:
        tmp += num - 1
        tmp %= k
        acc.append(tmp)
    ans = 0
    df = {}
    for i in range(n + 1):
        if not acc[i] in df:
            df[acc[i]] = 1
        else:
            df[acc[i]] += 1
        ans += (df[acc[i]] - 1)
        if i >= k-1:
            df[acc[i-k+1]] -= 1



    print(ans)
    # print(acc)
if __name__ == "__main__":
    main()