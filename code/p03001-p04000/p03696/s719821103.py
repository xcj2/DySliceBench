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


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
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


def test1(s):
    stack = deque()
    out = ''
    tmp = ''

    for i in range(len(s)):
        if s[i] == ')' and len(stack) == 1 and stack[-1] == '(':
            out += '(' + tmp + ')'
            tmp = ''
            stack.pop()
        elif s[i] == ')' and len(stack) > 0 and stack[-1] == '(':
            tmp = '(' + tmp + ')'
            stack.pop()
        elif s[i] == ')' and len(stack) == 0:
            tmp = '(' + tmp + ')'
        else:
            stack.append('(')
            out += tmp
            tmp = ''

    for i in range(len(tmp)//2):
        out = '(' + out + ')'

    tmp = ''
    while len(stack) > 0:
        tmp = '(' + tmp + ')'
        stack.pop()

    out += tmp

    return out


def test2(s):
    stack = deque()
    out = ''
    tmp = ''

    for i in range(len(s)):
        if s[i] == ')' and len(stack) > 0 and stack[-1] == '(':
            tmp = '(' + tmp + ')'
            stack.pop()
        elif s[i] == ')' and len(stack) == 0:
            tmp = '(' + tmp + ')'
        else:
            stack.append('(')
            out += tmp
            tmp = ''
        # print('out', out)
        # print(tmp)

    out += tmp

    tmp = ''
    while len(stack) > 0:
        tmp = '(' + tmp + ')'
        stack.pop()

    out += tmp

    return out


def main():
    N = I()
    s = S()
    c = 0
    stack = deque()

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
            c += 1
        elif len(stack) > 0:
            stack.pop()
            c -= 1
        else:
            c += 1

    # print(c, stack)
    print('(' * (c - len(stack)) + s + ')' * len(stack))

    # print('out1', out1)
    # print('out2', out2)

    # print(sorted([out1, out2])[0])


if __name__ == '__main__':
    main()
