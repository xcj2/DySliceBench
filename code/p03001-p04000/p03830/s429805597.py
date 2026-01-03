from collections import defaultdict
import sys
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
            
N=int(input())
mod=10**9+7
if N==1:
    print(1)
    sys.exit()
A=Prime(10**3+1)
dd=defaultdict(int)
for i in range(2,N+1):
    for p,j in A.decom(i).items():
        dd[p]+=j
ans=1
for j in dd.values():
    ans*=j+1
    ans%=mod
print(ans)