import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    def factorization(n):
        if n==1:
            return []
        arr = []
        temp = n
        for i in range(2, int(-(-n**0.5//1))+1):
            if temp%i==0:
                cnt=0
                while temp%i==0:
                    cnt+=1
                    temp //= i
                arr.append([i, cnt])

        if temp!=1:
            arr.append([temp, 1])

        if arr==[]:
            arr.append([n, 1])

        return arr
    
    mod=10**9+7
    a,b=MI()
    from math import gcd
    g=gcd(a,b)
    arr=factorization(g)
    
    ans=len(arr)+1
    
    print(ans)
    
    
    

main()
