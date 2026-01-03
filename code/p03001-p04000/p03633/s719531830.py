# https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0
# abcde	s=input()	s='abcde'
# abcde	s=list(input())	s=['a', 'b', 'c', 'd', 'e']
# 5(1つだけ)	a=int(input())	a=5
# 1 2	| x,y = map(int,input().split())   |	x=1,y=2
# 1 2 3 4 5 ... n 　	li = input().split()	li=['1','2','3',...,'n']
# 1 2 3 4 5 ... n 　	li = list(map(int,input().split()))	li=[1,2,3,4,5,...,n]
# FFFTFTTFF 　	li = input().split('T')	li=['FFF', 'F', '', 'FF']

# INPUT
# 3
# hoge
# foo
# bar
# ANSWER
# n=int(input())
# string_list=[input() for i in range(n)]


from collections import defaultdict, Counter
import math
from bisect import bisect_left, bisect_right
import numpy as np

# a, bの最大公約数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

# a, bの最小公倍数
def lcm(a, b):
    return int(a * b) // gcd(a,b)

# リストnumbers最小公倍数
def lcmlist(numbers):
    a = numbers[0]
    for i in range(1, len(numbers)):
        a = lcm(a, numbers[i])
    return int(a)

#### START
n = int(input())
t = [int(input()) for i in range(n)]

print(lcmlist(t))
