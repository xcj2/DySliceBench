MOD=1000000007
def fact(x):
    k=1
    for i in range(x+1):
        if i!=0:
            k=(k*i)%MOD
    return k

def inverse(b):
    r=1;e=MOD-2
    while e:
        if (e%2==1):
            r = (r*b)%MOD
        b=(b*b)%MOD
        e>>=1
    return r

def Comb(i,j):
    if i==0 or j==0:
        return 0
    num=fact(i+j)
    num*=inverse(fact(i))
    num%=MOD
    num*=inverse(fact(j))
    num%=MOD
    return num
    
r1,c1,r2,c2 = map(int,input().split())
#おなじみパスカル行列を区間で和を取ろうという問題
#F[n][r]=nCr(n+r,r)と、
#G[a][b]をΣ[i,0~a-1](Σ[j,0~b-1](F[i][j]))と表す
#ここで、G[a][b]をO(N)くらいで計算できれば勝ち
#ところで、G[a][b]=F[a+1][b+1]-1になる
#なので、それぞれのGをO(N+logMOD)で計算できるのでAC
Ans=0
Ans+=Comb(r2+1,c2+1)
Ans-=Comb(r1,c2+1)
Ans-=Comb(r2+1,c1)
Ans+=Comb(r1,c1)
Ans+=MOD;Ans+=MOD;Ans%=MOD

print(Ans)