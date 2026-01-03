class Prime:
    def __init__(self,number):#N以下の素数
        self.jud=[True]*(number+5)
        self.pri=[]
        self.jud[0]=False
        self.jud[1]=False
        for i in range(number):
            if self.jud[i]:
                self.pri.append(i)
                for j in range(2,(number-1)//i+1):
                    self.jud[i*j]=False
    
    def judge(self,x):
        return self.jud[x]
    
    def decom(self,x):
        s=x
        a =[]
        if s==1:
            return a
        while s>1:
            for p in self.pri:
                if s%p==0:
                    a.append(p)
                    s=s//p
                    break
        return a
            

from collections import defaultdict
dd=defaultdict(int)
N = int(input())
mod =10**9+7
P=Prime(10**3)
for i in range(1,N+1):
    for s in P.decom(i):
        dd[s]+=1
ans = 1
for i in dd.values():
    ans *= i+1
    ans %= mod
print(ans)