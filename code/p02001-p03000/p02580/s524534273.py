import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W,M=MI()
    nh=[0]*H
    nw=[0]*W
    
    from collections import defaultdict
    dd = defaultdict(int)
    
    for i in range(M):
        h,w=MI()
        h-=1
        w-=1
        dd[(h,w)]=1
        nh[h]+=1
        nw[w]+=1
        
    Mh=max(nh)
    Mw=max(nw)
    
    if Mh==0:
        print(Mw)
    elif Mw==0:
        print(Mh)
    else:
        ans=Mh+Mw-1#交差するところに爆弾があったと仮定する．なければあとで+1
        
        hh=[]
        ww=[]
        for i in range(H):
            if nh[i]==Mh:
                hh.append(i)
        
        for i in range(W):
            if nw[i]==Mw:
                ww.append(i)
                
        for h in hh:
            for w in ww:
                if dd[(h,w)]==0:
                    ans+=1
                    print(ans)
                    exit()
        print(ans)
                

main()
