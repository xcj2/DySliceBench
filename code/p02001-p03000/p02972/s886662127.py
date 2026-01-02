def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
import copy
def divisor(n): #約数
    f=[]
    d=[1]
    c=0
    r=int(n**0.5)
    for i in range(2,r+2):
        while n%i==0:
            c+=1
            n=n//i
        if c!=0:
            f.append([i,c])
            c=0
    if n!=1:
        f.append([n,1])
    for i in range(len(f)):
        t=[]
        for j in range(1,f[i][1]+1):
            t.append(f[i][0]**j)
        for j in range(len(d)):
            for k in range(len(t)):
                d.append(d[j]*t[k])
    return sorted(d)
n=I()
A=IL()
Ans=copy.deepcopy(A)
AA=[0]*n
AAA=[0]*n
last=-1
first=n
ans=0
c=True
while first>0:
    last=first
    first=first//2
    for i in range(first,last):
        if A[i]==1:
            if AA[i]==1:
                c=False
                break
            AA[i]=1
            L=divisor(i+1)
            for l in L:
                if A[l-1]==0:
                    A[l-1]=1
                else:
                    A[l-1]=0
                    
                if AAA[l-1]==0:
                    AAA[l-1]=1
                else:
                    AAA[l-1]=0   
                

if AAA!=Ans or not c:
    print(-1)
    print(A)
else:
    print(sum(AA))
    for i in range(n):
        if AA[i]==1:
            print(i+1,end=" ")
    print()