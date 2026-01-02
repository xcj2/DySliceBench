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
#n,k= (int(i) for i in input().split())      #入力整数横2つ
#x,y,z = (int(i) for i in input().split())    #入力整数横3つ
#n,m,x,y= (int(i) for i in input().split())  #入力整数横4つ
#a = [int(i) for i in input().split()]        #入力整数配列
#a = input()                                  #入力文字列
#a = input().split()                          #入力文字配列

#jの変数はしようできないので注意
a =[]
for i in range(3):
    a.append(input())
sum = 0
for i in range(x):
    b = [a[0][i],a[1][i],a[2][i]]
    b.sort()
    if b[0] == b[1] or b[1]==b[2]:
        if b[0] == b[1] and b[1]==b[2]:
            f =0
        else: sum+=1
    else: sum+=2
print(sum)