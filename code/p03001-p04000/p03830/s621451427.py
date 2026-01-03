def make_divisors(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if(n%i==0):
            divisors.append(i)
            divisors.append(n//i)
    return divisors
    
def factorization(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct
    
def main():
    n=int(input())
    ans=1
    cnt={}
    for i in range(1,n+1):
        fact=factorization(i)
        for s in fact:
            if s not in cnt:
                cnt[s]=1
            else:
                cnt[s]+=1
    for value in cnt.values():
        ans=ans*(value+1)%(10**9+7)
    print(ans)
main()
    
    