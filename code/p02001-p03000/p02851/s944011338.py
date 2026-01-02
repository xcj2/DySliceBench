import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))


"""
N^2なので素直に計算は無理，部分和を使いたいのでとりあえず累積和
[i+1:j]が条件を満たすとはS[j]-S[i]とj-iが合同．
移行して，S[j]-jとS[i]-iが合同
基本は個数だけ見れば良い

これだけだと，個数がKより大きい時にダメ
直近Kこの情報だけ持つ，今見てる数字が直近K個のものと何個組にできるか
"""
def main():

    mod=10**9+7
    N,K=MI()
    A=LI()
    from collections import defaultdict
    dd = defaultdict(int)
    
    S=[0]*(N+1)
    for i in range(N):
        S[i+1]=(S[i]+A[i])%K
        
    ans=0
    for i in range(min(K,N+1)):
        temp=(S[i]-i)%K
        ans+=dd[temp]
        dd[temp]+=1
        
    for i in range(K,N+1):
        temp=(S[i]-i)%K
        temp_m=(S[(i-K)]-(i-K))%K
        dd[temp_m]-=1
        ans+=dd[temp]
        dd[temp]+=1
        
    print(ans)
        
        
    

        

main()
