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


def S(): return input()


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def main():
    st = S()
    Q = I()
    queries = []
    # print(st[0])
    # s = [st[i] for i in range(len(st))]
    s = deque()

    for i in range(len(st)):
        s.append(st[i])

    for i in range(Q):
        queries.append(list(MS()))

    op = True

    for i in range(Q):
        query = queries[i]
        if len(query) == 1:
            op = not op
        else:
            if (query[1] == '1' and op is True) or (query[1] == '2' and op is False):
                s.appendleft(query[2])
            elif (query[1] == '1' and op is False) or (query[1] == '2' and op is True):
                s.append(query[2])
            else:
                exit(-1)
                return

    # print(op)
    if op is True:
        print(''.join(s))
    else:
        n = []
        while len(s):
            n.append(s.pop())
        print(''.join(n))


if __name__ == '__main__':
    main()
