def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

from collections import defaultdict
from sys import exit
import math


def main():
    n, m = getList()
    nums = getList()
    tree = [[] for _ in range(n)]
    for i in range(m):
        # start, end, cost
        a, b = getList()
        # 0-indexed
        a -= 1
        b -= 1
        tree[a].append(b)
        tree[b].append(a)
    ans = 0
    for i, t in enumerate(tree):
        cur = nums[i]
        fl = True
        for ne in t:
            if nums[ne] >= cur:
                fl = False

        if fl:
            ans += 1

    print(ans)
if __name__ == "__main__":
    main()