a,b=map(int,input().split())

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return int(a*b/gcd(a,b))

g=gcd(a,b)
def prime_factorization(n):
    #nを素因数分解して、昇順のリストを返す
    m=n
    ans = []
    p = 2

    while p<m**0.5:
        if n%p == 0:
            ans.append(p)
            while n%p==0:
                n /= p
        else:
            p += 1
            
    if n!=1:
        ans.append(int(n))
    
    return ans

l=prime_factorization(g)
print(len(l)+1)
