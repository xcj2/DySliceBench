import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    
    def F(a,b):
        na=len(str(a))
        nb=len(str(b))
        return max(na,nb)
    
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)

        # divisors.sort()
        return divisors
    
    L=make_divisors(N)
    ans=10**10
    for i in range(len(L)):
        a=L[i]
        b=N//L[i]
        temp=F(a,b)
        ans=min(ans,temp)
        
    print(ans)
        
        

main()
