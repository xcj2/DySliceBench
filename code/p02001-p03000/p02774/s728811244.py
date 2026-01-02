import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def find_x_miman(pos, i, neg, x):
    if len(neg) == 0:
        return 0
    if neg[0] * pos[i] >= x:
        return 0
    ok = 0
    ng = len(neg)
    while ok + 1 < ng:
        m = (ng + ok) // 2
        if neg[m] * pos[i] < x:
            ok = m
        else:
            ng = m
    return ok + 1

def find_x_miman_from_right(arr, i, x):
    if not (i + 1  < len(arr)):
        return 0
    if arr[i] * arr[i+1] >= x:
        return 0

    ok = i + 1
    ng = len(arr)
    while ok + 1 < ng:
        m = (ng + ok) // 2
        if arr[m] * arr[i] < x:
            ok = m
        else:
            ng = m
    return ok - i

def main():
    N, K = LI()
    A = LI()
    A = sorted(A)
    pos = [a for a in A if a > 0]
    neg = [a for a in A if a < 0]
    rev_neg = [abs(a) for a in neg][::-1]
    n_zero = N - len(neg) - len(pos)
    l = -10**18 - 1 # K未満
    r = 10**18 + 1

    def count_miman(x):
        # return count of mul less than x
        cnt = 0
        if x < 0:
            for i in range(len(pos)):
                cnt += find_x_miman(pos, i, neg, x)
        else: # x > 0
            if x > 0:
                cnt += n_zero * (len(neg) + len(pos)) + (n_zero * (n_zero - 1)) // 2
            for i in range(len(pos)):
                cnt += find_x_miman_from_right(pos, i, x)
            for i in range(len(rev_neg)):
                cnt += find_x_miman_from_right(rev_neg, i, x)
            cnt += len(pos) * len(neg)
        return cnt

    # x未満がK個未満あるような最大のx
    while l + 1 < r:
        m = (l + r) // 2
        mimcount = count_miman(m)
        if mimcount < K:
            l = m
        else:
            r = m
    print(l)

main()

