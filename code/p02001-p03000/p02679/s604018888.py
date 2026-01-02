from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product, combinations_with_replacement
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
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def print_matrix(mat):
    for i in range(len(mat)):
        print(*['IINF' if v == IINF else "{:0=4}".format(v) for v in mat[i]])


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
show_flg = False
# show_flg = True

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    N = I()
    zero = 0
    plus_Ai_Bi = defaultdict(int)
    minus_Bj_Aj = defaultdict(int)
    zero_cnt = 0
    used = set()

    for i in range(N):
        a, b = MI()

        if a == 0 and b == 0:
            zero_cnt += 1
            continue

        gcdab = gcd(abs(a), abs(b))
        a = a // gcdab
        b = b // gcdab

        if a > 0 and b > 0:
            # pos
            plus_Ai_Bi[(a, b)] += 1
            # neg
            minus_Bj_Aj[(-b, a)] += 1
        elif a > 0 and b < 0:
            # neg
            plus_Ai_Bi[(-a, -b)] += 1
            # pos
            minus_Bj_Aj[(-b, a)] += 1
        elif a < 0 and b > 0:
            # neg
            plus_Ai_Bi[(a, b)] += 1
            # pos
            minus_Bj_Aj[(b, -a)] += 1
        elif a == 0:
            # neg
            plus_Ai_Bi[(a, abs(b))] += 1
            # pos
            minus_Bj_Aj[(abs(b), a)] += 1
        elif b == 0:
            # neg
            plus_Ai_Bi[(abs(a), b)] += 1
            # pos
            minus_Bj_Aj[(b, abs(a))] += 1
        else:
            # pos
            plus_Ai_Bi[(-a, -b)] += 1
            # neg
            minus_Bj_Aj[(b, -a)] += 1

    # print(plus_Ai_Bi)
    # print(minus_Bj_Aj)
    ans = 1

    for pair, cnt1 in plus_Ai_Bi.items():
        a, b = pair
        if pair in used:
            continue

        if pair in minus_Bj_Aj:
            cnt2 = minus_Bj_Aj[pair]
            group1 = pow(2, cnt1, MOD) - 1
            group2 = pow(2, cnt2, MOD) - 1
            ans *= group1 + group2 + 1
            ans %= MOD

            if a > 0 and b > 0:
                # minus_Bj_Aj[(-b, a)] += 1
                used.add((-b, a))
            elif a > 0 and b < 0:
                # minus_Bj_Aj[(-b, a)] += 1
                used.add((-b, a))
            elif a < 0 and b > 0:
                # minus_Bj_Aj[(b, -a)] += 1
                used.add((b, -a))
            elif a == 0:
                used.add((abs(b), a))
            elif b == 0:
                used.add((b, abs(a)))
            else:
                # minus_Bj_Aj[(b, -a)] += 1
                used.add((b, -a))
            # print(pair, ans)
        else:
            ans *= pow(2, cnt1, MOD)
            ans %= MOD

    print((ans - 1 + zero_cnt) % MOD)


if __name__ == '__main__':
    main()
