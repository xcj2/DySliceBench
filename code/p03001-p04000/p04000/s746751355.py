import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W,N=MI()
    B=set([])
    from collections import defaultdict
    used = defaultdict(int)
    ans=[0]*10
    
    for _ in range(N):
        a,b=MI()
        a-=1
        b-=1
        B.add((a,b))
        
    def cnt(i,j):#i,jが左上の9ます
        if i+2<H and j+2<W:
            temp=0
            for di in range(3):
                for dj in range(3):
                    ii=i+di
                    jj=j+dj
                    if (ii,jj) in B:
                        temp+=1
            used[(i,j)]=1
            return temp
        return -1
    
    def se(i,j):#i,jが中心の25ます
        for di in range(-2,1,1):
            for dj in range(-2,1,1):
                ii=i+di
                jj=j+dj
                if ii>=0 and jj>=0:
                    if not used[(ii,jj)]:
                        cc=cnt(ii,jj)
                        if cc!=-1:
                            #print(ii,jj,cc)
                            ans[cnt(ii,jj)]+=1
                        
    for k in B:
        i,j=k[0],k[1]
        se(i,j)
        
    S=sum(ans)
    ans[0]=(H-2)*(W-2) - S
    for i in range(10):
        print(ans[i])
                    

main()
