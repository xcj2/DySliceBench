def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

from collections import defaultdict, Counter
from sys import exit
import math


def main():
    n = getN()
    nums = getList()
    den = [num - i for i, num in enumerate(nums)]
    cnt = Counter(den)
    ans = 0
    for i in range(n-1):
        k1, k2 = nums[i], nums[i+1]
        su = k1 + k2
        tgt = den[i+1] - su + 1
        if tgt in cnt.keys():
            ans += cnt[tgt]
    print(ans)
if __name__ == "__main__":
    main()