import sys
input = sys.stdin.readline

def main():
    def I(): return int(input())
    def MI(): return map(int, input().split())
    def LI(): return list(map(int, input().split()))
    mod=10**9+7
    """
    kを決めるかxを決めるか，
    kを決めればxが一意に決まり，N個試してO(N^2)
    xを決めればどうなるんだろう．
    ai全部にxorして，それをずらせばbになるならok．なんかもう少しうまくできそう．
    
    解説読んだ.
    全部のところに同じ操作をしている=>2箇所を使うことでうまく追加分を打ち消すことを考える．
    隣接2箇所を選びxorすれば xor xの部分が消える（もし+xなら2箇所選んで引けば良いというお話）
    
    shiftしたものが一致するか知る方法=>aとbなら，a*2の中にbがあるか探す．ここでKMP法やz-algoritmを使う
    
    
    """
    
    def Z(s):
        n=len(s)
        lcp=[0]*n
        lcp[0]=n
        L,R=0,0
        for i in range(1,n):
            if(i>=R): # 過去の結果の再利用が不可
                L=i
                R=i
                while(R<n and s[R-L]==s[R]):
                    R+=1
                lcp[i]=R-L
            elif(lcp[i-L]<R-i): # 過去の結果を再利用
                lcp[i]=lcp[i-L]
            else: # 過去の結果を一部再利用
                L=i
                while(R<n and s[R-L]==s[R]):
                    R+=1
                lcp[i]=R-L
        return lcp
    
    N=I()
    a=LI()
    b=LI()
    a+=[a[0]]
    b+=[b[0]]
    
    #隣接二項のxorがrotateしてることが必要
    a2=[0]*N
    b2=[0]*N
    for i in range(N):
        a2[i]=a[i+1]^a[i]
        b2[i]=b[i+1]^b[i]
        
    #a2*2の中にb2があるか見たい，abbに対してZしてi>=Nで，LCPがN以上の場所
    
    K=[]
    abb=a2+b2+b2
    L=Z(abb)
    
    for i in range(N,2*N,1):
        if L[i]>=N:
            K.append((2*N-i)%N)
            
    X=[]
    for k in K:
        x=b[0]^a[k]
        X.append(x)
    
    if K!=[]:
        K,X=zip(*sorted(zip(K,X)))
    else:
        exit()
        
    for i in range(len(K)):
        print(K[i],X[i])
        

    

main()
