def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W,K=MI()
    S=[[]for _ in range(H)]
    for i in range(H):
        S[i]=list(input())
        
    ans=10**10
    
    import itertools
    import bisect
    
    for ite in itertools.product([0,1], repeat=H):
        #高さ方向で全探索，0,1の切り替わりでグループを分ける
        g=[]#各グループの末尾列の番号
        cnt=[]#数えるよう,合計
        cnt2=[]#数えるよう,その列だけ
        now=-1
        for i in range(len(ite)):
            if ite[i]!=now:
                g.append(i-1)
                cnt.append(0)
                cnt2.append(0)
                now=ite[i]
        g.append(H-1)
        cnt.append(0)
        cnt2.append(0)
        temp=len(g)-2
        last=[0]#最後に追ったところを保存
        fl=0#Kを超えたら
        fl2=0#無理なとき
        for j in range(W):
            for k in range(len(cnt2)):
                cnt2[k]=0
            if fl2==1:
                break
            for i in range(H):
                if S[i][j]=="1":
                    num=bisect.bisect_left(g,i)
                    cnt[num]+=1
                    cnt2[num]+=1
                    if cnt[num]>K:
                        fl=1
                    
            if fl==1:
                for k in range(len(cnt)):
                    cnt[k]=cnt2[k]
                    cnt2[k]=0
                fl=0
                temp+=1
                last.append(j)
                if last[-1]==last[-2]:
                    temp=10**10
                    fl2=1
                    break
                
        #print(ite,temp,g,last)
        ans=min(ans,temp)
        
    print(ans)
                
                
                    
                    
                
        
        
    

main()
