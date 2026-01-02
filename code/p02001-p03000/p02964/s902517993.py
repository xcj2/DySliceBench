import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    A=LI()
    if N==1:
        if K%2==0:
            ans=[]
            print(' '.join(map(str, ans)))
        else:
            print(A[0])
    else:
        #有向グラフ
        #i番目からスタートした時，次の週のときにどこからスタートしたものと同様になるか，を追えば良い
        #例えば，12323ならば2週目の最初に1が出たときに実質リセットされるので2323をみるのと同じになる
        #これは結局，次に自分と同じ番号が出てくるところの次，なければループ
        M=2*(10**5)
        L=[[]for _ in range(M+1)]#各数字がどこに出てくるか記録
        
        A=A+A+A
        for i in range(N*3):
            L[A[i]].append(i)
            
        nxt=[0]*(N+1)
        
        import bisect
        for i in range(N-1,-1,-1):
            num=bisect.bisect_right(L[A[i]],i)
            nxt_st=L[A[i]][num]
            if nxt_st>=N:
                if nxt_st==2*N-1:
                    nxt[i]=N
                else:
                    nxt[i]=nxt_st+1-N
            else:
                if nxt_st==N-1:
                    nxt[i]=N
                nxt[i]=nxt[(nxt_st+1)%N]
            # print(A[i])
            # print(L[A[i]])
            # print(num)
            # print(nxt_st)
            # print(nxt[i])
            # print("----")
            
        #nxtがわかればあとはダブリング
        N2=50
        dub=[[0]*(N+1) for _ in range(N2)]#最後に注意．1,2,3で3から始めたら次は無
        for i in range(N):#最後はどうせ０なので無視
            dub[0][i]=i
            dub[1][i]=nxt[i]

        
        for j in range(1,N2-1):
            for i in range(N+1):
                dub[j+1][i]=dub[j][dub[j][i]]
                
        # for j in range(10):
        #     print(dub[j])
        
        st=0
        K-=1#このdubやnxtは，次の時にどこから始まるかなので-1
        for j in range(1,N2):#0の時はいらない
            if K&1:
                st=dub[j][st]
            K=K>>1
            
        if st==N:
            ans=[]
            print(' '.join(map(str, ans)))
        else:

            
            ans=[]
            from collections import defaultdict
            dd = defaultdict(int)
            
            for i in range(st,N):
                if dd[A[i]]:
                    x=-1
                    while x!=A[i]:
                        x=ans.pop()
                        dd[x]=0
                else:
                    ans.append(A[i])
                    dd[A[i]]=1
                    
            print(' '.join(map(str, ans)))
        
    
    
    

main()
