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

x = ip()                              #入力整数1つ
#x,y= (int(i) for i in input().split())      #入力整数横2つ
#x,y,z = (int(i) for i in input().split())    #入力整数横3つ
#n,m,x,y= (int(i) for i in input().split())  #入力整数横4つ
a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列

#jの変数はしようできないので注意
num=0
while sum(a):
    l = 0
    while a[l] == 0: l+=1
    r=l
 #   print("left:",l)
    if l != len(a)-1:
        while a[r+1]!=0:
 #           print("right:",r)
            r+=1
            if r == len(a)-1:break
    for i in range(l,r+1):
        a[i]-=1
    num+=1
  #  print(a)
print(num)
