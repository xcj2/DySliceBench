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
    if q==1: print("Yay!")
    else:print(":(")
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
#n = ip()                                     #入力整数1つ
#n,q= (int(i) for i in input().split())       #入力整数横2つ以上
#a = [int(i) for i in input().split()]        #入力整数配列
#b = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
a=[ip() for i in range(5)]    #入力セット(整数改行あり)(2/2)
#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
#こっから本文
ms = [a[i]%10 for i in range(5)]
for i in range(5):
    if ms[i]==0:ms[i]+=10
p = ms.index(min(ms))
b = []
for i in range(5):
    if i==p:
        b.append(a[i])
    elif a[i]%10:
        b.append(a[i]//10*10+10)
    else: b.append(a[i])
print(sum(b))