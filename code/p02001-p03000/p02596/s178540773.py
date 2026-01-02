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

def count_ones(n):

    # to store number of 1s
    # in smallest repunit
    # multiple of the number.
    count = 1;

    # initialize rem with 1
    rem = 7

    if n == 7:
        return 1

    # run loop until
    # rem becomes zero
    while rem != 0:
        # rem*10 + 1 here represents
        # the repunit modulo n
        # print((rem * 10 + 7))
        rem = (rem * 10 + 7) % n
        count = count + 1

        if count > 10 ** 6:
            count = -1
            break

    # when remainder becomes
    # 0 return count
    return count

def main():
    K = I()
    MAX = 10 ** 6

    if K % 2 == 0:
        print(-1)
        return

    if K == 1:
        print(1)
        return

    print(count_ones(K))



if __name__ == '__main__':
    main()
