def s0():return input()
def s1():return input().split()
def s2(n):return [input() for x in range(n)]
def n0():return int(input())
def n1():return [int(x) for x in input().split()]
def n2(n):return [int(input()) for _ in range(n)]
def n3(n):return [[int(x) for x in input().split()] for _ in range(n)]

from collections import deque 
s=s0()
n=n0()
q=s2(n)

d1=deque()
d2=deque()

f=False
for a in q:
    if a[0]=="1":
        f=not(f)
    else:
        if a[2]=="1":
            if f==False:
                d1.appendleft(a[4])
            else:
                d2.append(a[4])                
        else:
            if f==False:
                d2.append(a[4])
            else:
                d1.appendleft(a[4])
ss=''.join(list(d1))+s+''.join(list(d2))
print(ss[::-1] if f else ss)