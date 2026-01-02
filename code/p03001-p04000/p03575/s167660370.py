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

n,m = ips()
a = []
s = 0
for i in range(m):
    x,y = ips()
    a.append([x,y])
connection = [[] for i in range(n+1)]
for i in range(m):
    [x,y] = a[i]
    connection[x].append(y)
    connection[y].append(x)
for loop in range(50):
    for i in range(1,n+1):
        if len(connection[i]) == 1:
            temp = connection[i][0]
            d = connection[temp].index(i)
            connection[temp].pop(d)
            s+=1
            connection[i].pop(0)
print(s)