from collections import defaultdict
class Prime:
    def __init__(self,number):#N以下の素数
        self.jud=[True]*(number+5)
        self.pri=[]
        self.jud[0]=False
        self.jud[1]=False
        for i in range(number):
            if self.jud[i]:
                self.pri.append(i)
                for j in range(2,(number)//i+1):
                    self.jud[i*j]=False
    
    def judge(self,x):
        return self.jud[x]
    
    def decom(self,x):
        s=x
        a =defaultdict(int)
        if s==1:
            return a
        while s>1:
            for p in self.pri:
                if s%p==0:
                    a[p]+=1
                    s=s//p
                    break
        return a
            

A=Prime(102+5)
N=int(input())
dd=defaultdict(int)
for s in range(2,N+1):
    d1=A.decom(s)
    for p,v in d1.items():
        dd[p]+=v
ans=0
#3-5-5type
L=[0,0]
for p,v in dd.items():
    if 2<=v<4:
        L[0]+=1
    elif 4<=v:
        L[1]+=1
ans+=(L[0]*L[1]*max(L[1]-1,0))//2
ans+=(L[1]*max(L[1]-1,0)*max(L[1]-2,0))//2
#print(ans)
#15-5type
M=[0,0]
for p,v in dd.items():
    if 4<=v<14:
        M[0]+=1
    elif 14<=v:
        M[1]+=1
ans+=M[0]*M[1]
ans+=(M[1]*max(M[1]-1,0))
#print(ans)
#25-3type
N=[0,0]
for p,v in dd.items():
    if 2<=v<24:
        N[0]+=1
    elif 24<=v:
        N[1]+=1
ans+=N[0]*N[1]
ans+=(N[1]*max(N[1]-1,0))
for p,v in dd.items():
    if 74<=v:
        ans+=1
print(ans)