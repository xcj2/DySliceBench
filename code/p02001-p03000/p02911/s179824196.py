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
def ipmultiplerow(n):
    a = []
    for i in range(n):
        a.append(ip())
    return a
def printrow(a):
    for i in a:
        print(i)


n,k,q = ips()
a = ipmultiplerow(q)
c = [0 for i in range(n)]
for i in range(q):
    c[a[i]-1]+=1
for i in c:
    if k-q+i>0:print("Yes")
    else:print("No")