import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    ans=1
    A.sort()
    L=[]
    if N%2==1:
        L.append(0)
        for i in range(N//2):
            for _ in range(2):
                L.append(2*(i+1))
                
    else:
        for i in range(N//2):
            for _ in range(2):
                L.append(2*i+1)
                
    if L==A:
        ans=pow(2,N//2,mod)
    else:
        ans=0
        
    print(ans)
        

main()
