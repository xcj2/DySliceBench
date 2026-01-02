from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
import sys
import bisect
import string
import math
import time


def I(): return int(input())


def MI(): return map(int, input().split())


def S(): return input()


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = {False: 'No', True: 'Yes'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False


def main():
    N, K = MI()
    s = S()
    a = [0]
    first_zero = s[0] == '0'
    cur = s[0]

    for i in range(len(s)):
        if cur == s[i]:
            a[-1] += 1
        else:
            cur = s[i]
            a.append(1)

    # print(a)
    # print(first_zero, limit)
    ans = 0
    cur = 0
    right = 0
    for left in range(len(a)):
        if first_zero:
            if left % 2 == 0:
                limit = 2 * K
            else:
                limit = 2 * K + 1
        else:
            if left % 2 == 0:
                limit = 2 * K + 1
            else:
                limit = 2 * K
        # limit = 2 * K if first_zero else 2 * K + 1

        while right < len(a) and right - left < limit:
            cur += a[right]
            right += 1

        ans = max(cur, ans)
        cur -= a[left]
        # print(ans, cur, cur + a[left], left, right)

    print(ans)


if __name__ == '__main__':
    main()
