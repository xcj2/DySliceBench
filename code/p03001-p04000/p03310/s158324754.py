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


def main():
    N = I()
    A = LI()
    cumsum = [0 for _ in range(N+1)]

    for i in range(N):
        cumsum[i+1] = cumsum[i] + A[i]

    def get_cumsum(a, b):
        # get cumsum from [a, b] element
        return cumsum[b+1] - cumsum[a]

    def separate_opt_sum(l, r, offset):
        tot_sum = get_cumsum(l, r)
        targ = offset + tot_sum / 2
        left_i = bisect.bisect_left(cumsum, targ)

        diff1 = inf
        diff2 = inf
        diff3 = inf
        left_sum1, right_sum1, left_sum2, right_sum2 = inf, inf, inf, inf
        left_sum3, right_sum3 = inf, inf

        if l <= left_i - 2:
            left_sum3 = get_cumsum(l, left_i - 2)
            right_sum3 = tot_sum - left_sum3
            diff3 = abs(right_sum3 - left_sum3)

        if l <= left_i - 1:
            left_sum1 = get_cumsum(l, left_i - 1)
            right_sum1 = tot_sum - left_sum1
            diff1 = abs(right_sum1 - left_sum1)

        if left_i < r:
            left_sum2 = get_cumsum(l, left_i)
            right_sum2 = tot_sum - left_sum2
            diff2 = abs(right_sum2 - left_sum2)

        if min(diff1, diff2, diff3) == diff1:
            return left_sum1, right_sum1
        elif min(diff1, diff2, diff3) == diff2:
            return left_sum2, right_sum2
        return left_sum3, right_sum3

    def _separate_opt_sum(l, r):
        # find arr1, arr2 s.t. |arr1 - arr2| = min
        # arr1 = get_cumsum(l, k), arr2 = get_cumsum(k+1, r)
        tot_sum = get_cumsum(l, r)
        m = (l + r) // 2
        m_min = l - 1
        m_max = r + 1
        cur_min_diff = abs(2 * get_cumsum(l, m) - tot_sum)
        cur_min_m = m
        while m_min < m and m < m_max:
            left_sum = get_cumsum(l, m)
            right_sum = tot_sum - left_sum
            cur_diff = abs(left_sum - right_sum)
            if cur_diff < cur_min_diff:
                cur_min_diff = cur_diff
                cur_min_m = m
            if left_sum < right_sum:
                m_min = m
                m = (m + r) // 2
            elif left_sum > right_sum:
                m_max = m
                m = (l + m) // 2
            else:
                break
        l_ans = get_cumsum(l, cur_min_m)
        r_ans = get_cumsum(cur_min_m + 1, r)
        return l_ans, r_ans

    ans = inf
    for sep in range(1, N-2):
        left_S = get_cumsum(0, sep)
        right_S = get_cumsum(sep+1, N-1)
        # import pdb
        # pdb.set_trace()
        p, q = separate_opt_sum(0, sep, 0)
        r, s = separate_opt_sum(sep+1, N-1, left_S)
        
        # print('sep:', sep, ' ', p, q, r, s)
        # print('\tleft_S:', left_S, ' right_S:', right_S)
        ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)
main()

