# https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0
# abcde	s=input()	s='abcde'
# abcde	s=list(input())	s=['a', 'b', 'c', 'd', 'e']
# 5(1つだけ)	a=int(input())	a=5
# 1 2	| x,y = s_inpl()   |	x=1,y=2
# 1 2 3 4 5 ... n 　	li = input().split()	li=['1','2','3',...,'n']
# 1 2 3 4 5 ... n 　	li = inpl()	li=[1,2,3,4,5,...,n]
# FFFTFTTFF 　	li = input().split('T')	li=['FFF', 'F', '', 'FF']

# INPUT
# 3
# hoge
# foo
# bar
# ANSWER
# n=int(input())
# string_list=[input() for i in range(n)]

import math
import numpy as np
import copy
from collections import defaultdict, Counter
from itertools import product
from bisect import bisect_left, bisect_right

def s_inpl(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))

N, X = s_inpl()
x = inpl()

x_diff = [ abs(X - xi) for xi in x]

# a, bの最大公約数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

# リストnumbers最大公約数
def gcdlist(numbers):
    a = numbers[0]
    for i in range(len(numbers)):
        a = gcd(a, numbers[i])
    return a

print(gcdlist(x_diff))