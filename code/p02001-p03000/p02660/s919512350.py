import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
        
    N=I()
    n=int(N**0.5)+1
    ans=0
    
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)

        # divisors.sort()
        return divisors
    
    div=make_divisors(N)
    if len(div)==2:
        ans+=1
    else:
        ans=0
        for d in div:
            div2=make_divisors(d)
            if N==0:
                break
            if len(div2)==2:
                p=div2[-1]
                p2=p
                while N%p2==0:
                    N=N//p2
                    p2*=p
                    ans+=1

        
            
    
    
            
    print(ans)

main()
