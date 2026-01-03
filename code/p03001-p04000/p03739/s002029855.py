import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    a=LI()
    ans=10**30
    aaa=[-1,1]
    
    for j in range(2):
        pos=aaa[j]
        S=0
        temp=0
        for i in range(N):
            S+=a[i]
            if S>0:
                Sp=1
            elif S<0:
                Sp=-1
            else:
                Sp=0
            
            
            if Sp!=pos*(-1):
                target=-1*pos
                temp+=abs(target-S)
                S=target
            pos*=-1
        ans=min(ans,temp)
        
    print(ans)
        
        

main()
