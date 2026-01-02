import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    import heapq
    from collections import defaultdict
    dd = defaultdict(int)
    
    N=I()
    A=LI()
    B=LI()
    
    cntA=[0]*(N+1)
    cntB=[0]*(N+1)
    
    for i in range(N):
        cntA[A[i]]+=1
        cntB[B[i]]+=1
        
    cnt=[0]*(N+1)
    # 合計がNより多いと無理
    for i in range(N+1):
        v1=cntA[i]
        v2=cntB[i]
        if v1+v2>N:
            print("No")
            exit()
        cnt[i]=v1+v2
        
    hqa=[]
    heapq.heapify(hqa)
    hqb=[]
    heapq.heapify(hqb)
    
    for i in range(N+1):
        if cntA[i]!=0:
            a=(-1*cntA[i],i)#回数*-1 , 値
            
            heapq.heappush(hqa,a)
        if cntB[i]!=0:
            a=(-1*cntB[i],i)#回数*-1 , 値
            
            heapq.heappush(hqb,a)
            
    L=[]#(aの値,bの値)を入れていく
    
    
    same=-1
    while hqa:
        ca,a=heapq.heappop(hqa)
        cb,b=heapq.heappop(hqb)
        
        
        #違うのなら組にできる
        if a!=b:
            use=max(ca,cb) * -1
            for _ in range(use):
                L.append((a,b))
                
            ca+=use
            if ca!=0:
                heapq.heappush(hqa,(ca,a))
            cb+=use
            if cb!=0:
                heapq.heappush(hqb,(cb,b))
                
        else:
            if not hqb:
                #取り出せないなら
                #つまり,b側は残り1種類

                use=ca*(-1)
                cb+=use
                heapq.heappush(hqb,(cb,b))
                for _ in range(use):
                    L.append((a,a))
                same=a
                
            else:
                (cb2,b2)=heapq.heappop(hqb)
                heapq.heappush(hqb,(cb,b)) #使わなかったやつ返す
                
                
                use=max(ca,cb2) * -1
                
                for _ in range(use):
                    L.append((a,b2))
                    
                ca+=use
                if ca!=0:
                    heapq.heappush(hqa,(ca,a))
                cb2+=use
                if cb2!=0:
                    heapq.heappush(hqb,(cb2,b2))
                
    L.sort()
    ans=[0]*N
    
    samex=[]
    nots=[]
    
    for i in range(N):
        temp=L[i][1]
        ans[i]=temp
        
        if A[i]==same and ans[i]==same:
            samex.append(i)
            
    for i in range(N):
        if A[i]!=same and ans[i]!=same:
            nots.append(i)

            
    if same!=-1:
        # if len(nots)<len(samex):
        #     print("No")
        #     exit()
        
        for i in range(len(samex)):#入れ替える
            ans[samex[i]],ans[nots[i]] = ans[nots[i]], ans[samex[i]]
            
    now=0
    aaa=0
    for i in range(N):
        if ans[i]==A[i]:
            for j in range(N-1,-1,-1):
                aaa+=1
                if A[j]!=ans[i] and A[i]!=ans[j]:
                    ans[i],ans[j] = ans[j],ans[i]
                    now=j
                if aaa>=100000000:
                    print("No")
                    exit()

        
        
    print("Yes")
    print(' '.join(map(str, ans)))
                
            


main()
