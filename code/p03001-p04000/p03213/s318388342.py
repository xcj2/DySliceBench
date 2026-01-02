import math
import copy

def ord(N,n):#N,nは正の整数、Nで割り切れる回数、許容はN^1000
    if n%N!=0:
        return 0
    else:
        return 1+ord(N,n//N)

def primenubertable(N):#素数表　１００００ぐらいまでは時間内に計算できそう
    import math
    X=[1]*N
    X[0]=0
    X[1]=0
    i=2
    P=[]
    while math.sqrt(N)>=i:
        if X[i]==1:
            for j in range(i+1,N):
                if j%i==0:
                    X[j]=0
        i=i+1
    for i in range(0,N):
        if X[i]==1:
            P.append(i)
    return P

def factor(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factor(n-1)

A=int(input())

N=factor(A)
P=primenubertable(100)
order=[]

for i in range(0,len(P)):
    x=ord(P[i],N)
    order.append(x)
a=0
b=0
c=0
d=0
e=0
for i in range(0,len(order)):
    if order[i]>=2:
        a=a+1
    if order[i]>=4:
        b=b+1
    if order[i]>=14:
        c=c+1
    if order[i]>=24:
        d=d+1
    if order[i]>=74:
        e=e+1
D=b*(b-1)//2
answer=D*(a-2)+c*(b-1)+d*(a-1)+e
print(answer)
