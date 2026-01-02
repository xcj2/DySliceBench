from statistics import mean, median,variance,stdev
import numpy as np
import sys
import math
import fractions
import itertools

def j(q):
    if q==1: print("Yes")
    else:print("No")
    exit(0)


def ct(x,y):
    if (x>y):print("")
    elif (x<y): print("")
    else: print("")

def ip():
    return int(input())

def swap(s,pos):
    s[pos]-=1
    s[pos+1]+=1
    print(s)
    if pos == n-2: return s
    if s[pos+2] == 0: swap(s,pos+1)
    return s


#n = ip()                              #入力整数1つ
#left,n= (int(i) for i in input().split())      #入力整数横2つ
n,x,y = (int(i) for i in input().split())    #入力整数横3つ
#n,m,x,y= (int(i) for i in input().split())  #入力整数横4つ
#a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[ip() for i in range(n)]    #入力セット(整数改行あり)(2/2)



#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
n-=y
print(n//(x+y))