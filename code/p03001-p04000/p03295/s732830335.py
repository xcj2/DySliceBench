import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    #左から見て，できるだけ右できる
    N,M=MI()
    ab=[[0,0]for _ in range(M)]
    for i in range(M):
        ab[i][0],ab[i][1]=MI()
        
    ab.sort(key=lambda x:(x[0],-1*x[1]))
    ans=0
    
    left=-1
    right=N+1
    for i in range(M):
        if ab[i][0]>=right:
            left=ab[i][0]
            right=ab[i][1]
            ans+=1
        else:
            left=ab[i][0]
            right=min(right,ab[i][1])
            
    print(ans+1)
            

main()
