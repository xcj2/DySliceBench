from statistics import mean, median,variance,stdev
import numpy as np
import sys
import math
import fractions
import itertools
import copy
import collections
from operator import itemgetter
#以下てんぷら
def j(q):
    if q==1: print("Yes")
    else:print("No")
    exit(0)


def ct(x,y):
    if (x>y):print("+")
    elif (x<y): print("-")
    else: print("?")

def ip():
    return int(input())
def printrow(a):
    for i in range(len(a)):
        print(a[i])
def combinations(n,r):
    if n<r:return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def permutations(n,r):
    if n<r:return 0
    return math.factorial(n) // math.factorial(n - r)

n = ip()                                     #入力整数1つ
#n,k= (int(i) for i in input().split())       #入力整数横2つ以上
#a = [int(i) for i in input().split()]        #入力整数配列
# a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#k = ip()                      #入力セット(整数改行あり)(1/2)
a=[ip() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#a=[input() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
#こっから本文
a.sort()
s = 0
cnum = a[0]
csum = 1
for i in range(1,n):
    if a[i] == cnum:
        csum+=1
    else:
  #      print(csum)
        cnum = a[i]
        s+=(csum%2)
        csum=1
  #  print(s,csum)
s+=(csum%2)
print(s)