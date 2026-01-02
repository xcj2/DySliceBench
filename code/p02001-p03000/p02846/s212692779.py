import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    T=LI()
    A=LI()
    B=LI()
    
    
    d1=(A[0]-B[0])*T[0]
    d2=(A[1]-B[1])*T[1]
    
    if d1>=0:
        #最初は必ず正の方向へいかないように調整
        d1*=-1
        d2*=-1
        
    
    if d1+d2==0:
        print("infinity")
    elif d1==0:#d1=0のパターンを排除した
        print(0)
    elif d1+d2<=0:
        print(0)
    else:
        cnt=(-1*d1)//(d1+d2)
        ans=cnt*2+1
        if cnt*(d1+d2)==-1*d1:
            ans-=1
        print(ans)
        
        
        
    

main()
