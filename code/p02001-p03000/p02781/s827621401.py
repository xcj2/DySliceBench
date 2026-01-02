N=int(input())
K=int(input())
import math
ans=0
n=str(N)
a=len(n)
def combi(p,q):
    if p<q : return 0
    else: return math.factorial(p)//(math.factorial(q)*math.factorial(p-q))
def mi(i):
    if i==0:
        return 0
    else:
        return i-1
def zero(i):
    if int(n[i])==0:
        return 0
    else:
        return 1
if a<K:
    ans=0
else:
    if a>K:
        ans+=combi(a-1,K)*(9**K)
    if K==1:ans+=int(n[0])
    elif K==2:
        x=0
        i=1
        b=0
        bs=0
        while True:
            if (int(n[i])!=0) and (x==0):
                b=int(n[i])
                bs=a-i
                x+=1
            if (x==1) or (i==len(n)-1):
                break
            i+=1
        ans+=mi(int(n[0]))*(a-1)*9+mi(bs)*9+b
    elif a==3 : ans+=mi(int(n[0]))*81*(combi(a-1,2))+9*mi(int(n[1]))+int(n[2])
    else:
        x=0
        i=1
        b=0
        bs=0
        c=0
        cs=0
        while True:
            if (int(n[i])!=0) and (x==0):
                b=int(n[i])
                bs=a-i
                x+=1
            elif (int(n[i])!=0) and (x==1):
                c=int(n[i])
                cs=a-i
                x+=1
            if (x==2) or (i==len(n)-1):
                break
            i+=1
        ans+=mi(int(n[0]))*81*(combi(a-1,2))+combi(bs-1,2)*81+9*(a-2)*mi(b)+c+mi(cs)*9

print(ans)
