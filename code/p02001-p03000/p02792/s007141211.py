import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    
    def ht(x):
        t=x%10
        string=str(x)
        h=int(string[0])
        return (h,t)
        
    cnt=[[0]*10 for _ in range(10)]
    
    for i in range(1,N+1):
        h,t=ht(i)
        cnt[h][t]+=1
        
    ans=0
    for i in range(10):
        for j in range(10):
            a=cnt[i][j]
            b=cnt[j][i]
            ans+=a*b
            
    print(ans)
        

main()
