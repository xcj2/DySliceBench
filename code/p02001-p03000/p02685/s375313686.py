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
MOD = 998244353
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
show_flg = False
# show_flg = True

g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル


# MOD 組み合わせ
def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


def main():
    N, M, K = MI()

    for i in range(2, N + 1):
        g1.append((g1[-1] * i) % MOD)
        inverse.append((-inverse[MOD % i] * (MOD//i)) % MOD)
        g2.append((g2[-1] * inverse[-1]) % MOD)

    ans = 0
    for k in range(K+1):
        group_color = M * pow(M - 1, N - k - 1, MOD)
        group_number = cmb(N-1, k, MOD)
        ans += (group_color * group_number) % MOD

    print(ans % MOD)


if __name__ == '__main__':
    main()
