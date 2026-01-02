import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    D=LI()
    M=I()
    T=LI()
    
    from collections import defaultdict
    dd = defaultdict(int)
    
    for i in range(N):
        dd[D[i]]+=1
        
    flag=1
    for i in range(M):
        dd[T[i]]-=1
        
    for k,v in dd.items():
        if v<0:
            flag=0
            
    if flag:
        print("YES")
    else:
        print("NO")
    

main()
