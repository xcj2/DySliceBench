import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import bisect
import heapq
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**15

def main():
    n, k = getlist()
    nums = getlist()
    acc = {0: [0]}
    tmp = 0
    for i, num in enumerate(nums):
        tmp += num
        tmp %= k
        tgt = ((tmp - i -1  + k) % k)
        if tgt not in acc:
            acc[tgt] = [i+1]
        else:
            acc[tgt].append(i+1)
        # acc.append(tmp-i-1)

    # cnt = Counter(acc)
    ans = 0
    for v in acc.values():
        for j, cur in enumerate(v):
            ins = bisect.bisect_left(v, cur+k)
            # print(ins, j)
            ans += ins - j - 1
        # ans += ((v-1) * v) // 2
    # print(acc)
    print(ans)

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""