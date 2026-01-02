#--import&define---------------------
import math

def yes():
    print("Yes")
def no():
    print("No")

def gusu(n):
    a = 0
    x = int(n/2)-1
    for i in range(x+1):
        if l[i]!=l[n-i-1]:
            a = a+1
    return a

def kisu(n):
    a=0
    x = int(n/2)-1
    for i in range(x+1):
        if l[i]!=l[n-i-1]:
            a = a+1
    return a
#--my_library--------------------------------
#mapを利用した入力
# x,y = map(int,input().split())

#forを利用した入力
#l = []
#for i in range():
#    l.append(int(input()))
#--以下解答---------------------------------
s = input()
l =list(s)
ans = 0

i=0
n=len(l)
flag = False

#偶数か奇数か見分ける
if n%2 == 0:
    flag = True

if flag == True:
    ans = gusu(n)
else:
    ans = kisu(n)

print(ans)

