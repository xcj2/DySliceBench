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
#b = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[ip() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
#こっから本文
one = 0
two = 0
four = 0
leftover = 0
for i in range(n):
    if a[i]%2: one+=1
    elif a[i]%4==0:four+=1
    else: two+=1
if one==1:
    if four==0:j(0)
    if one == four: leftover = 1
    if two%2:
        if leftover==0:
            j(0)
        else:j(1)
    else: j(1)

if one-1 > four:j(0)
else :
    if one==four:leftover=1
    if two%2:
        if leftover==0:
            j(0)
        else:j(1)
    else: j(1)