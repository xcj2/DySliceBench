import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=998244353
    N=I()
    A=LI()
    MA=max(A)
    x=[0]*(MA+1)
    
    #数列x[i]はi*(iの個数)
    for i in range(N):
        x[A[i]]+=A[i]
        
    #print(x)
    
    #上位集合のゼータ変換
    for k in range(1,MA+1):
        for s in range(k*2,MA+1,k):#sが2kからkずつ増える=>sはkの倍数(自分自身を数えないため，2kから)
            x[k]=(x[k]+x[s])%mod
    
    #print(x)
    #この段階でx[i]はiを約数に持つやつの和(個数も加味している)
    
    #積演算
    for i in range(MA+1):
        x[i]=(x[i]*x[i])%mod
        
    #print(x)
    
    
    #メビウス変換で戻す
    for k in range(MA,0,-1):
        for s in range(k*2,MA+1,k):
            x[k]=(x[k]-x[s])%mod
            
    #この段階でx[i]はiをgcdに持つもの同士をかけたものの和
    #print(x)
    
    #gcdでわる
    ans=0
    for i in range(1,MA+1):
        if x[i]!=0:
            x[i]=(x[i]*pow(i,mod-2,mod))%mod
            ans=(ans+x[i])%mod
        
    #この段階でx[i]はiをgcdに持つもの同士のlcaの和
    #print(x)
        
    ans=(ans-sum(A))%mod
    #A[i],A[i]の組を除去する．A[i]動詞のくみはlcaがA[i]になる
       
    """ 
    ans=(ans*pow(2,mod-2,mod))%mod#A[i]*A[j] と　A[j]*A[i]の被り除去
    print(pow(2,mod-2,mod))=499122177
    """
    ans=(ans*499122177)%mod
    
    print(ans)
        
    
    

main()
