import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    
    N=I()
    #約数列挙
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)

        # divisors.sort()
        return divisors
    
    ans=set(make_divisors(N-1))
    ans=ans - set([1])
    ans.add(2)
    
    L=make_divisors(N)
    
    for i in range(1,len(L)):
        temp=L[i]
        N2=N
        while N2>=temp:
            if N2%temp==0:
                N2=N2//temp
            else:
                N2=N2%temp
        if N2==1:
            ans.add(temp)
            
        
            
    
    print(len(ans))

        

main()
