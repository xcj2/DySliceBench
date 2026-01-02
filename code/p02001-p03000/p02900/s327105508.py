def prime_factorize(N): 
    exponent = 0
    while N%2 == 0:
        exponent += 1
        N //= 2
    if exponent: factorization = [[2,exponent]]
    else: factorization = []
    i=1
    while i*i <=N:
        i += 2
        if N%i: continue
        exponent = 0
        while N%i == 0:
            exponent += 1
            N //= i
        factorization.append([i,exponent])
    if N!= 1: factorization.append([N,1])
    assert N != 0, "zero"
    return factorization

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def main():
    a,b = map(int,input().split())
    g = gcd(a,b)
    print(len(prime_factorize(g))+1)

if __name__ == "__main__":
    main()