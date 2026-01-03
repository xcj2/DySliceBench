import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,A,B=MI()
    h=[0]*N
    for i in range(N):
        h[i]=I()
        
    def ch(X):
        #X回で達成できるか?
        temp=0
        for i in range(N):
            hp=h[i]-X*B
            if hp>0:
                temp+=(hp+A-B-1)//(A-B)
        if temp<=X:
            return True
        return False
    
    ng=0
    ok=10**9
    
    while abs(ok-ng)>1:
        x=(ok+ng)//2
        if ch(x):
            ok=x
        else:
            ng=x
    print(ok)
        

main()
