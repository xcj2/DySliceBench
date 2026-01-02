from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
import math
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
#####################################
def convert(x):
    if x==0:
        return "0"
    s=""
    while(x):
        r=x%2
        x//=2
        s=str(r)+s
    return s
def binary(m,size):
    s=convert(m)
    s=(size-len(s))*"0"+s
    return s
r,c,k=INPUT()
A=[]
for i in range(r):
    x=input()
    A.append(list(x))

rowblack=[]#all the sum of the rows r
for i in range(r):
    sum=0
    for j in range(c):
        if A[i][j]=="#":
            sum+=1
    rowblack.append(sum)
columnblack=[]
for i in range(c):
    sum=0
    for j in range(r):
        if A[j][i]=="#":
            sum+=1
    columnblack.append(sum)

Rows=[]
for i in range(2**r):
    Rows.append(binary(i,r))
Columns=[]
for j in range(2**c):
    Columns.append(binary(j,c))

ans=0
def count(l,m,A):
    c=0
    for i in range(len(l)):
        if int(l[i])==0:
            for j in range(len(m)):
                if int(m[j])==0:
                    if A[i][j]=="#":
                        c+=1
    #print(c)
    return c

for i in range(len(Rows)):
    for j in range(len(Columns)):
        if count(Rows[i],Columns[j],A)==k:
            ans+=1
print(ans)
