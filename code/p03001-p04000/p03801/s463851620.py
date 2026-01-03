from collections import defaultdict
import sys
class BIT():
    def __init__(self, number):
        self.n = number
        self.list = [0] * (number + 1)

    def add(self, i, x):  # ith added x  1indexed
        while i <= self.n:
            self.list[i] += x
            i += i & -i

    def search(self, i):  # 1-i sum
        s = 0
        while i > 0:
            s += self.list[i]
            i -= i & -i
        return s

    def suma(self, i, j):  # i,i+1,..j sum
        return self.search(j) - self.search(i - 1)

N=int(input())
A=[int(i) for i in input().split()]
C=sorted(set(A))
ndd=defaultdict(int)
for i in range(len(C)):
    ndd[i+1]=C[i]
dd=defaultdict(int)
for i in range(len(C)):
    dd[C[i]]=i+1
#print(ndd,dd)
visit=[0]*N
visit[0]=1
s=A[0]
H=[]
H.append(s)
for i in range(1,N):
    if s<A[i]:
        s=A[i]
        H.append(s)
        visit[i]=1

BITI=BIT(N+1)
BITI2=BIT(N+1)
j=len(H)-1
l=dd[H[j]]
num=sum(A)
T=[0]*N
ans=0
for i in range(N-1,-1,-1):
    if l==dd[A[0]]:
        break
    BITI.add(dd[A[i]],A[i])
    BITI2.add(dd[A[i]],1)
    if dd[A[i]]==l and visit[i]==1:
        T[i]=BITI.suma(dd[H[j-1]],N+1)-BITI2.suma(dd[H[j-1]],N+1)*H[j-1]-ans
        ans+=T[i]
        #print(i,j,l,T[i],ans)
        j-=1
        l=dd[H[j]]
x=num-sum(T)
T[0]=x
#print(visit,T)
for t in T:
    print(t)




