from statistics import mean, median,variance,stdev
import numpy as np
import sys
import math
import fractions
import itertools
import copy
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

def pne(n):
    print(n,end='')

rem = pow(10,9)+7

n = ip()                                     #入力整数1つ
k = ip()
#a,b,c= (int(i) for i in input().split())       #入力整数横2つ以上
a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[input() for i in range(n)]    #入力セット(文字列改行あり)(2/2)
#a=[ip() for i in range(n)]    #入力セット(整数改行あり)(2/2)

#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
#こっから本文
#''' なんだかんだ必要じゃねと思って残す複数入力
s = 0
for i in range(n):
    s+= 2*min(abs(k-a[i]),a[i])
print(s)
