# from https://atcoder.jp/contests/dp/submissions/4751518
import sys
input=sys.stdin.readline
from collections import deque

def check(l0,l1,l2):
    return (l2[1]-l1[1])*(l1[0]-l0[0])>=(l1[1]-l0[1])*(l2[0]-l1[0])

def f(l,x):
    return l[0]*x+l[1]

def add_line(a,b):
    while len(deq)>=2 and check(deq[-2],deq[-1],(a,b)):
        deq.pop()
    deq.append((a,b))

def query(x):
    while len(deq)>=2 and f(deq[0],x)>=f(deq[1],x):
        deq.popleft()
    return f(deq[0],x)


n,c=map(int,input().split())
h=[int(i) for i in input().split()]
d=[0]*n
deq=deque()
add_line(-2*h[0],h[0]**2+d[0])
for i in range(1,n):
    d[i]=query(h[i])+h[i]**2+c
    add_line(-2*h[i],h[i]**2+d[i])
print(d[-1])
