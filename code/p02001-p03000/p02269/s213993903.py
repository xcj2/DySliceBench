
def h1(key):
    return key%m

def h2(key):
    return 1+(key%(m-1))

def h(key,i):
    return (h1(key)+i*h2(key))%m

def insert(t,key):
    i=0
    while True:
        j=h(key,i)
        if t[j]==-1:
            t[j]=key
            return j
        else:
            i+=1

def search(t,key):
    i=0
    while True:
        j=h(key,i)
        if t[j]==key:
            return j
        elif t[j]==-1 or i>=m:
            return -1
        else:
            i+=1

def change(c):
    ans=""
    for i in range(len(c)):
        if c[i]=="A":
            ans+="1"
        if c[i]=="C":
            ans+="2"
        if c[i]=="G":
            ans+="3"
        if c[i]=="T":
            ans+="4"
    return int(ans)

m=1046527
n=int(input())
dict=[-1]*m
import sys
input=sys.stdin.readline
for _ in range(n):
    l=list(input().split())
    k=change(l[1])
    if l[0]=="insert":
        insert(dict,k)
    else:
        if search(dict,k)!=-1:
            print("yes")
        else:
            print("no")

