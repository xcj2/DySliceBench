import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001



line = []

def calc_E(left,right):
    global line

    depth = 0
    Q = deque()

    #深さ0の、プラスまたはマイナスを探す(単項の-は無いものとする)
    i = left
    while i <= right:
        if line[i] == '(':
            depth += 1
        elif line[i] == ')':
            depth -= 1

        if depth != 0:
            i += 1
        elif line[i] != '+' and line[i] != '-':
            i += 1
        else:
            Q.append(i)
            i += 1

    if len(Q) == 0:
        return calc_T(left,right)

    tmp = calc_E(left,Q[0]-1)

    while len(Q) > 0:
        loc = Q.popleft()

        tmp_right = None

        if len(Q) == 0:
            tmp_right = calc_T(loc+1,right)
        else:
            tmp_right = calc_T(loc+1,Q[0]-1)

        if line[loc] == '+':
            tmp += tmp_right
        else:
            tmp -= tmp_right

    return tmp


def calc_T(left,right):
    global line

    depth = 0
    Q = deque()

    #深さ0の、*または/を探す
    i = left
    while i <= right:
        if line[i] == '(':
            depth += 1
        elif line[i] == ')':
            depth -= 1

        if depth != 0:
            i += 1
        elif line[i] != '*' and line[i] != '/':
            i += 1
        else:
            Q.append(i)
            i += 1

    if len(Q) == 0:
        return calc_F(left,right)

    tmp = calc_T(left,Q[0]-1)

    while len(Q) > 0:
        loc = Q.popleft()

        tmp_right = None

        if len(Q) == 0:
            tmp_right = calc_F(loc+1,right)
        else:
            tmp_right = calc_F(loc+1,Q[0]-1)

        if line[loc] == '*':
            tmp *= tmp_right
        else: #注意:たとえば(-3//2はpython3では-2になる模様)
            if tmp*tmp_right > 0:
                tmp = abs(tmp)//abs(tmp_right)
            else:
                tmp = abs(tmp)//abs(tmp_right)
                tmp *= -1

    return tmp


def calc_F(left,right):
    if line[left].isdecimal():
        return calc_NUM(left,right)
    elif line[left] == '(':

        depth = 0
        close_pos = None

        for i in range(left,right+1):
            if line[i] == '(':
                depth += 1
            elif line[i] == ')':
                depth -= 1
                if depth == 0:
                    close_pos = i
                    break

        return calc_E(left+1,close_pos-1)

def calc_NUM(left,right):
    global line
    ret = 0

    for i in range(left,right+1):
        ret = 10*ret+int(line[i])

    return ret

N = int(input())

for _ in range(N):
    line = str(input())
    print("%d"%(calc_E(0,len(line)-2)))


