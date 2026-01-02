# -*- coding: utf-8 -*-
'''
所要時間は、分位であった。
'''


# ライブラリのインポート
#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
from collections import deque
#import math

def main():
    n = int(input())
    for _ in range(n): 
        IN = input().strip()
        exp1 = calcmold(IN)
        exp2 = calc1(exp1)
        exp3 = calcmult(exp2)
        print(calcplus(exp3))

def calcmold(exp):
    # seikei
    tmp = ""
    EXP = deque()
    oplist = ["+","-","*","/","(",")","="]
    for i in range(len(exp)):
        if exp[i] not in oplist:
            tmp += exp[i]
        else:
            if tmp == "":
                EXP.append(exp[i])
                continue
            EXP.append(int(tmp))
            EXP.append(exp[i])
            tmp = ""
    return EXP


def calc1(IN):
    #calculate()
    EXP = deque()
    while(IN):
        check = IN.popleft()
        if check == ")":
            TMP = deque()
            while(1):
                look = EXP.pop()
                if look == "(": break
                TMP.appendleft(look)
            TMP.append("=")
            EXP.append(calcplus(calcmult(TMP)))
        else: EXP.append(check)
    return EXP
        


def calcmult(exp):
    # no()
    EXP = deque()
    while(exp):
        check = exp.popleft()
        if check == "*":
            arg1 = EXP.pop()
            arg2 = exp.popleft()
            EXP.append(arg1*arg2)
        elif check == "/":
            arg1 = EXP.pop()
            arg2 = exp.popleft()
            EXP.append(int(arg1/arg2))
        else: EXP.append(check)
    return EXP


def calcplus(exp):
    # no()
    EXP = deque()
    while(exp):
        check = exp.popleft()
        if check == "+":
            arg1 = EXP.pop()
            arg2 = exp.popleft()
            EXP.append(arg1+arg2)
        elif check == "-":
            arg1 = EXP.pop()
            arg2 = exp.popleft()
            EXP.append(arg1-arg2)
        elif check == "=":
            return EXP.pop()
        else: EXP.append(check)
    return EXP
if __name__ == '__main__':
    main()

