import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque, Counter
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
INF = 10 ** 9

def main():
    n = getN()
    nums = getList()
    tmp = 1
    br = n
    for num in (nums):
        # print(num, tmp)
        if num == tmp:
            br -= 1
            tmp += 1
            # print(br, num)



    if br == n:
        ans = -1
    else:
        ans = br
    print(ans)

if __name__ == "__main__":
    main()