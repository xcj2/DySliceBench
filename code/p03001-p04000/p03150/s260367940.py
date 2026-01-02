from statistics import mean, median,variance,stdev
import sys
import math
import fractions

def j(q):
    if q==1: print("YES")
    else:print("NO")
    exit(0)


def ct(x,y):
    if (x>y):print("")
    elif (x<y): print("")
    else: print("")

def ip():
    return int(input())

#x = ip()                              #入力整数1つ
#x,y= (int(i) for i in input().split())      #入力整数横2つ
#x,y,z = (int(i) for i in input().split())    #入力整数横3つ
#n,m,x,y= (int(i) for i in input().split())  #入力整数横4つ
#x = [int(i) for i in input().split()]        #入力整数配列
a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列
l = len(a)
p = 0
for i in range(l):
    b = a[:i]
    for z in range(l):
        c = a[z:]
        d = ''.join([b,c])
        if 'keyence' == d : j(1)
j(0)