import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W=MI()
    if (H*W)%3==0:
        print(0)
    else:
        def tw(h,w):
            #2つに分ける
            if (h*w)%2==0:
                return h*w//2,h*w//2
            else:
                a=h//2*w
                b=h*w - a
                c=w//2*h
                d=h*w - c
                if abs(a-b)<=abs(c-d):
                    return a,b
                else:
                    return c,d
                
            
        ans=10**10
        s=[0,0,0]
        #一個目を，長さW高さiにする，iを探索
        for i in range(1,H):
            s[0]=i*W
            s[1],s[2]=tw(H-i,W)
            temp=max(s)-min(s)
            ans=min(ans,temp)
            
        for j in range(1,W):
            s[0]=j*H
            s[1],s[2]=tw(H,W-j)
            temp=max(s)-min(s)
            ans=min(ans,temp)
        print(ans)
            
    
            

main()
