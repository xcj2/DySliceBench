import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,X,Y=MI()
    X-=1
    Y-=1
    
    ans=[0]*N
    
    for i in range(N):
        for j in range(i+1,N):
            if j<=X:
                d=j-i
            elif i>=Y:
                d=j-i
            elif i<=X and j>=Y:
                d=X-i + j-Y +1
            elif i<=X and j<=Y:
                d=min(j-i,X-i +1 +Y-j)
            elif i>=X and j>=Y:
                d=min(j-i, i-X +1 +j-Y)
            else:#どっちも内側
                d=min(j-i, i-X +1 +Y-j)
                
            ans[d-1]+=1
            
    for i in range(N-1):
        print(ans[i])
                

                
   

main()
