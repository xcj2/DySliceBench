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
H=list(map(int,input().split()))
DP=[0]*n
deq=deque()
add_line(-2*H[0],H[0]**2+DP[0])
for i in range(1,n):
    DP[i]=query(H[i])+H[i]**2+c
    add_line(-2*H[i],H[i]**2+DP[i])
print(DP[-1])