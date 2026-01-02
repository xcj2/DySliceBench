import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    L=LI()
    cnt=0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                a=L[i]
                b=L[j]
                c=L[k]
                if a!=b and b!=c and c!=a:
                    S=a+b+c
                    M=max(a,b,c)
                    if M<S-M:
                        cnt+=1
                    
                    
    print(cnt)

main()
