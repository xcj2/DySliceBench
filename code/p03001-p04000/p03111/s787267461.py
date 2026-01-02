from statistics import mean, median,variance,stdev
import numpy as np
import sys
import math
import fractions
import itertools

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

def swap(s,pos):
    s[pos]-=1
    s[pos+1]+=1
    print(s)
    if pos == n-2: return s
    if s[pos+2] == 0: swap(s,pos+1)
    return s


#n = ip()                              #入力整数1つ
#h,w= (int(i) for i in input().split())      #入力整数横2つ
#n,x,y = (int(i) for i in input().split())    #入力整数横3つ
n,a,b,c= (int(i) for i in input().split())  #入力整数横4つ
#a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
#n = ip()                      #入力セット(整数改行あり)(1/2)
#a=[ip() for i in range(n)]    #入力セット(整数改行あり)(2/2)

#jの変数はしようできないので注意
#全足しにsum変数使用はsum関数使用できないので注意
l = []
for i in range(n):
    l.append(ip())
if a in l and b in l and c in l:
    print(0)
    exit(0)
l.sort()
req = [a, b,c]
m  =set()
set = [0 for i in range(n)]
set[0] = -1
while sum(set) < n*3:
    while sum(set) < n*3:
        d = 0
        set[d]+=1
        while set[d] == 4:
            set[d]=0
            d+=1
            set[d]+=1
        if 0 in set and 1 in set and 2 in set: break
    if sum(set) != n*3:
        s = [0,0,0,0]
        mi = 0
        for i in range(n):
            s[set[i]]+= l[i]
        for i in range(3):
            mi += abs(s[i] - req[i]) + (set.count(i)-1) * 10
        m.add(mi)
print(min(m))