import sys
sys.setrecursionlimit(1000000)
from operator import *

ops = {'+':lambda x1, x2: x1 | x2, '*': lambda x1, x2: x1 & x2, '^': lambda x1, x2: x1 ^ x2}

def f(op, s1, s2):
    return ops[op](s1, s2)

def toN(s, numbers):
    for abc, number in zip(letters, list(numbers)):
        s = s.replace(abc, number)
    return s

letters = list("abcd")
def solve(S, P):
    origin = S
    S = S.replace('[', 'f(')
    S = S.replace(']', '),')
    for k in ops.keys():
        S = S.replace(k, "'" + k + "',")
    for l in letters:
        S = S.replace(l, l + ",")
    transed = S

    # print(S)
    res = eval(toN(S, P))[0]
    print(res, end=' ')
    count = 0
    for i in range(10000):
        if res == eval(toN(S, "{:04d}".format(i)))[0]:
            count += 1
    
    print(count)

while True:
    S = input()
    if S == '.':
        break
    P = input()
    solve(S, P)
