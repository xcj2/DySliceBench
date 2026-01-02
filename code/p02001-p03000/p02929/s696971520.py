

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()*2
    S=input()
    
    #括弧のように，各位置ごとに始まりか終わりかを規定
    #とじカッコの位置で，カッコを開いた数だけ通り数がある．
    
    st=list(range(N))
    for i in range(N):
        if S[i]=="B":
            c=0
        else:
            c=1
        st[i]=(st[i]+c)%2

    ans=1
    cnt=0#開き-閉じる
    
    for i in range(N):
        if st[i]==0:
            cnt+=1
        else:
            if cnt<0:
                ans=0
            ans=(ans*cnt)%mod
            cnt-=1
            
    #前半いらないが一応
    if st[-1]==0 or st[0]==1 or cnt!=0:
        ans=0
    for i in range(1,N//2+1):
        ans=(ans*i)%mod
    print(ans)
    
    
main()
