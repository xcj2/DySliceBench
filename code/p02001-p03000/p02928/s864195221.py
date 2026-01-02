import copy

def j(n):
    if n:print("Yes")
    else:print("No")
    exit(0)
rem = 10 ** 9 + 7

"""
def ct(x,y):
    if (x>y):print("+")
    elif (x<y): print("-")
    else: print("?")
"""

def ip():
    return int(input())
def iprow():
    return [int(i) for i in input().split()]
def ips():
    return (int(i) for i in input().split())
def printrow(a):
    for i in a:
        print(i)
s = 0
n,r =ips()
a = iprow()
other=0
for i in range(n):
    for k in range(n):
        if a[i]>a[k] and i<k:
            s+=1
        elif i>k and a[i]>a[k]:
            other+=1
adder = 0
rate = s
ans = 0
ans =((s + (s * r)) * r)//2 + ((other + other*(r-1)) * (r-1))//2
print(ans%rem)
