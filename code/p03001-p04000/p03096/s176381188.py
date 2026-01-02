import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    C=[]
    
    #連番無視
    for i in range(N):
        c=I()
        c-=1
        if C==[]:
            C.append(c)
        else:
            if C[-1]!=c:
                C.append(c)         
            
    """
    i番目の通り数をf(i)とする．
    今，i番目までを見てて，i番目と同じ数はj,kにあるとする．
    f(i)=
         f(i-1) #iを使わない
        +f(j-1) #i-jのみ
        +f(k-1) #i-kのみ
    かな，各色ごとに，f(j-1)+f(k-1)みたいなのをまとめておく
    """    
    S=[0]*(2*10**5 + 5)
    
    ans=1
    for c in C:
        temp=ans
        ans=(ans+S[c])%mod
        S[c]=(S[c]+temp)%mod
        
    print(ans)
        
        
        
        
    

main()
