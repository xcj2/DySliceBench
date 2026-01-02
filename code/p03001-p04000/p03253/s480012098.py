import copy

N,M=map(int,input().split())
mod=10**9+7

#x以下の素数の列挙   
import math
x=math.floor(math.sqrt(10**9))
L=math.floor(math.sqrt(x))#平方根を求める
Primelist=[i for i in range(x+1)]
Primelist[1]=0#素数でないものは0にする.
for i in Primelist:
    if i>L:
        break
    if i==0:
        continue
    for j in range(2*i,x+1,i):
        Primelist[j]=0
Primes=[Primelist[j] for j in range(x+1) if Primelist[j]!=0]

def fact(M):#約数の列挙
    if M==1:
        return {1}
    
    DICT=dict()#素因数分解
    i=0
    while M!=1 and i<len(Primes):
        if M%Primes[i]==0:
            DICT[Primes[i]]=DICT.get(Primes[i],0)+1
            M=M//Primes[i]
        else:
            i+=1

    if M!=1:
        DICT[M]=1

    VALUES=list(DICT.values())
    KEYS=list(DICT.keys())

    LIST=[1]

    for i in range(len(DICT)):
        NOWLIST=copy.copy(LIST)
        for l in NOWLIST:
            for j in range(0,VALUES[i]+1):
                LIST.append(l*KEYS[i]**j)

    return set(LIST)

def Combi2(a,b):#aは大きいが、bは小さいとき
    if b>a:
        return 0
    ANS=1
    for i in range(min(b,a-b)):
        ANS=ANS*(a-i)%mod*pow(min(b,a-b)-i,mod-2,mod)%mod

    return ANS%mod



SET=fact(M)
factor=dict()

for j in SET:
    factor[j]=fact(j)

DP=dict()
defaultans=[0 for i in range(40)]
defaultans[1]=1
defaultans=tuple(defaultans)

def dp(m):
    ANS=[0 for i in range(40)]
    if m==1:
        return defaultans
    
    for j in factor[m]:
        #print(j,factor[m])

        if j==1:
            continue
        else:
            if DP.get(m//j,-1)!=-1:
                NEXT=DP[m//j]
            else:
                NEXT=dp(m//j)

            for k in range(39):
                ANS[k+1]=(ANS[k+1]+NEXT[k])%mod

            #print(m//j,ANS,NEXT)

        DP[m]=ANS
    return ANS
            
LIST=dp(M)
ANS=0
for i in range(40):
    if LIST[i]!=0:
        ANS=ANS+Combi2(N,i-1)*LIST[i]%mod

print(ANS%mod)
