import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))


"""
「1回の握手でX以上幸福度が上がるならば採用」としたときに，何個採用することになるか？
此の値が初めてM以上になったところのXを利用すれば答えが出る．
例えばM+2開催消してしまったら，2*X引けば良い

「X以上なら採用」は左手ごとに，右手を二分探索

"""
def main():
    import bisect
    
    mod=10**9+7
    N,M=MI()
    A=LI()
    A.sort()
    
    def ch(X):
        temp=0
        
        for i in range(N):#左手
            l=A[i]
            t=X-l
            num=bisect.bisect_left(A,t)
            temp+=N-num
            
        return temp>=M
    
    
    ok=0
    ng=2*(10**5) + 1
    
    while ng - ok > 1:
        med=(ok+ng)//2
        if ch(med):
            ok=med
        else:
            ng=med
            
    # 総和の計算パート，累積和で
    S=[0]*(N+1)
    for i in range(N):
        S[i+1]=S[i]+A[i]
        
    ans=0
    temp=0
    X=ok
    for i in range(N):#左手
        l=A[i]
        t=X-l
        num=bisect.bisect_left(A,t)
        temp+=N-num
        ans+=S[-1] - S[num] + (N-num)*l
        # print(i,num,S[-1]-S[num],(N-num)*l)

        
    if temp>M:
        ans-=X*(temp-M)
        
    print(ans)
    
        
    
        
    
            
    
            
        
            

main()
