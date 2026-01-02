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
n = ip()                                     #入力整数1つ
#n,q= (int(i) for i in input().split())       #入力整数横2つ以上
a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[ip() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
#こっから本文
dlist = []
ulist = []
for i in range(n):
    if i%2:
        ulist.append(a[i])
    else: dlist.append(a[i])
ulist.sort()
dlist.sort()

firstupper = 0
secondupper = 0
maxupper = ulist[0]
maxlower = dlist[0]
c = 1
cnum = ulist[0]
for i in range(1,len(ulist)):
    if ulist[i] == cnum:
        c+=1
    else:
        cnum = ulist[i]
        if c > firstupper:
            maxupper = ulist[i-1]
            secondupper = firstupper
            firstupper = c
        elif c > secondupper and firstupper >= c:
            secondupper = c
        c = 1
if c > firstupper:
    maxupper = ulist[i-1]
    secondupper = firstupper
    firstupper = c
elif c > secondupper and firstupper >= c:
    secondupper = c


firstlower = 0
secondlower = 0
c = 1
cnum = dlist[0]
for i in range(1,len(dlist)):
 #   print("f",dlist[i])
    if dlist[i] == cnum:
        c+=1
    else:
        cnum = dlist[i]
        if c > firstlower:
            maxlower = dlist[i-1]
            secondlower = firstlower
            firstlower = c
        elif c > secondlower and firstlower >= c:
            secondlower = c
        c = 1
if c > firstlower:
  #  print("reqmet")
    maxlower = dlist[i-1]
    secondlower = firstlower
    firstlower = c
elif c > secondlower and firstlower >= c:
    secondlower = c
c = 0
"""
print(maxupper,maxlower)
print(firstupper,firstlower)
print(secondupper,secondlower)
"""
p = len(ulist)
if maxupper == maxlower:
    print(min(p-firstupper+p-secondlower,p-secondupper+p-firstlower))
else: print(2*p - firstupper - firstlower)
