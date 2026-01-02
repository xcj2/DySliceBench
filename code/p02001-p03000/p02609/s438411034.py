

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    def popcount(x):
        '''xの立っているビット数をカウントする関数
        (xは64bit整数)'''

        # 2bitごとの組に分け、立っているビット数を2bitで表現する
        x = x - ((x >> 1) & 0x5555555555555555)

        # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
        x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

        x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
        x = x + (x >> 8) # 16bitごと
        x = x + (x >> 16) # 32bitごと
        x = x + (x >> 32) # 64bitごと = 全部の合計
        return x & 0x0000007f
    
    N=I()
    Xst=input()
    
    #メモ化
    dp=[0]*(N+5)
    for i in range(1,N+5):
        X=i
        X=X%popcount(X)
        dp[i]=dp[X]+1 
       
    a=Xst.count("1")
    #a+1,a-1でしか割らない
    if a==0:
        for i in range(N):
            print(1)
        exit()
    elif a==1:
        for i in range(N):
            if Xst[i]=="1":
                print(0)
            else:
                if i!=(N-1):
                    print(1)
                else:
                    if Xst[-1]=="0":
                        print(2)
        exit()
    
    remp=[0]*(N+1)
    remm=[0]*(N+1)
    
    remp[0]=1%(a+1)
    remm[0]=1%(a-1)
    
    for i in range(1,N+1):#
        remp[i]=(2*remp[i-1])%(a+1)
        remm[i]=(2*remm[i-1])%(a-1)
    
    Xremp=0
    Xremm=0
    for i in range(N):
        if Xst[i]=="1":
            Xremp+=remp[N-i-1]
            Xremm+=remm[N-i-1]
    Xremp%=(a+1)
    Xremm%=(a-1)
    
    #print(Xremp,Xremm)
    
    for i in range(N):
        if Xst[i]=="0":
            Xrem2=(Xremp+remp[N-i-1])%(a+1)
        else:
            Xrem2=(Xremm-remm[N-i-1])%(a-1)
        
        print(dp[Xrem2]+1)
    
    
    
        

main()
