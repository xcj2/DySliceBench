import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    A=LI()
    CB=[[0,0]for _ in range(M)]
    A.sort()
    for i in range(M):
        CB[i][1],CB[i][0]=MI()
        
    CB.sort(reverse=True)
    now=0
    
    for i in range(N):
        if CB[now][1]<=0:
            now+=1
        
        if now>=M:
            break    
        
        ch=CB[now][0]
        if A[i]<ch:
            A[i]=ch
            CB[now][1]-=1
        else:
            break
        
    print(sum(A))
    

main()
