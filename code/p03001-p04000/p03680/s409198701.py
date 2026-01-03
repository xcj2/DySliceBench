from statistics import mean, median,variance,stdev
import numpy as np
import sys
import math
import fractions
import itertools
import copy

def j(q):
    if q==1: print("Heisei")
    else:print("TBD")
    exit(0)


def ct(x,y):
    if (x>y):print("")
    elif (x<y): print("")
    else: print("")

def ip():
    return int(input())


#n = ip()                              #入力整数1つ
#n,k= (int(i) for i in input().split())      #入力整数横2つ
#n,x,y = (int(i) for i in input().split())    #入力整数横3つ
#n,a,b,c= (int(i) for i in input().split())  #入力整数横4つ
#a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
n = ip()                      #入力セット(整数改行あり)(1/2)
a=[ip() for i in range(n)]    #入力セット(整数改行あり)(2/2)

#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
b = [[-1,-1]]
for i in range(n):
    b.append([i+1,a[i]])
c = 1
count = 0
while b[c][0] != -1:
    b[c][0] = -1
    count +=1
    c = b[c][1]
    if c == 2:
        print(count)
        exit(0)
print(-1)