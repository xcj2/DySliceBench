import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    n=I()
    s=I()
    
    if s==n:
        print(n+1)
    elif s>n:
        print(-1)
    else:
        #nをb進法にして，桁和を計算
        def calc(b,n):
            temp=0
            while n!=0:
                temp+=n%b
                n=n//b
            return temp
        
        ans=1000000000000
        N=1000000
        
        #まずはbを10**6程度まで探索
        for b in range(2,N):
            if calc(b,n)==s:
                ans=b
                break
            
        if ans!=1000000000000:
            print(ans)
            
        #もし，b>10**6で，うまく表現できるならばそれは2桁となる，b>10**6より，上位桁は最高でも10**6程度(max_n=10**11だから)
        else:
            #a1が上位の桁,a0が下位の桁
            for a1 in range(1,N):
                a0=s-a1
                if a0<0:
                    break
                if (n-a0)%a1==0:
                    b=(n-a0)//a1
                    if b>1000000 and a0<b and a1<b:
                        ans=min(ans,b)
                        
            if ans!=1000000000000:
                print(ans)
            else:
                print(-1)
        
        
    
    
    
    
    
    
            
    
        

main()
