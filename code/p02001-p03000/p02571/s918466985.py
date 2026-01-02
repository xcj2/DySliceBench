from sys import stdin, stdout
from collections import Counter,deque
import math
cin = stdin.readline
cout = stdout.write
def inpn():
    return(int(cin()))
def inpl():
    return(list(map(int,cin().split())))
def inps():
    return cin()[:-1]
def inpv():
    return (map(int, cin().split()))
def outs(s):
    cout(s)
def outn(n):
    cout(str(n))
def outl(l):
    for i in l:
        cout(str(i)+" ")
def outb(s):
    cout(str(s))


# n = inpn()
# l=inpl()
# m=1000000007
# add=0
# for i in range(n-1):
#     for j in range(i+1,n):
#         add+=(l[i]%m*l[j]%m)%m
#
# outn(add%m)
# cout("\n")

s=inps()
t=inps()
ans=1000
if t in s:
    outn(0)
    cout("\n")
else:
    if len(s)!=len(t):
        for i in range(len(s)-len(t)):
            count=0
            for j in range(len(t)):
                if s[i+j]!=t[j]:
                    count+=1
            ans=min(ans, count)
        outn(ans)
        cout("\n")
    else:
        ans=0
        for i in range(len(s)):
            if s[i]!=t[i]:
                ans+=1
        outn(ans)
        cout("\n")















