#071-D
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return input()
n=I()
s1=list(S())
s2=SL()
mod=pow(10,9)+7
s=[]
i=0
if n==1:
    ans=3
elif n==2:
    ans=6
else:
    while i<=n-2:
        if s1[i]==s1[i+1]:
            s.append(2)
            i+=2
        else:
            s.append(1)
            i+=1
    if s1[-1]!=s1[-2]:
        s.append(1)
    if s[0]==1:
        ans=3
    else:
        ans=6
    for i in range(1,len(s)):
        if s[i-1]==1:
            ans*=2
        else:
            if s[i]==2:
                ans*=3
        ans=ans%mod
print(ans)