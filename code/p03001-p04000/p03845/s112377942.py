from statistics import mean, median,variance,stdev
import numpy as np
import sys
import math
import fractions
import itertools
import copy

def j(q):
    if q==1: print("YES")
    else:print("NO")
    exit(0)


def ct(x,y):
    if (x>y):print("GREATER")
    elif (x<y): print("LESS")
    else: print("EQUAL")

def ip():
    return int(input())


def calculate(a):
    s = 0
    for i in range(len(a)):
        for k in range(i+1,len(a)):
            s+=(a[i]*a[k])
    return s

n = ip()                                     #入力整数1つ
#n,x= (int(i) for i in input().split())       #入力整数横2つ以上
t = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[ip() for i in range(n)]    #入力セット(整数改行あり)(2/2)
#a=[input() for i in range(h)]
#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
m  =  ip()
s = []
for i in range(m):
    a,b= (int(i) for i in input().split())
    c = copy.copy(t)
    c[a-1] = b
    s.append(sum(c))
for i in range(len(s)):
    print(s[i])