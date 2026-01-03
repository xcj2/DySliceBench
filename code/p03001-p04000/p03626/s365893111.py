import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    S1=input()
    S2=input()
    L=[0]
    
    #最初：0 縦向き:1 横向き:2
    i=0
    for _ in range(N):
        if S1[i]==S2[i]:
            L.append(1)
            i+=1
        else:
            L.append(2)
            i+=2
        if i>=N:
            break
    ans=1
    
    for i in range(1,len(L)):
        if L[i-1]==0:
            if L[i]==1:
                ans*=3
            else:
                ans*=6
        elif L[i-1]==1:
            ans*=2
        else:
            if L[i]==1:
                continue
            else:
                ans*=3
        ans%=mod
    print(ans)
        
    

main()
