def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def prime_factors(N): #素因数#エラーある
    ret = []
    middle = int( N**(1/2))
    tmp = N
    for i in range(2, middle+1):
        if tmp%i == 0:
            while tmp%i == 0:
                tmp //= i
            ret.append(i)
    if tmp != 1:
        ret.append(tmp)
    return ret


    
def main():
    a, b = map( int, input().split())
    d = gcd(a,b)
#    print(2, is_prime(2))
    if d == 1:
        print(1)
        return

    print(len(prime_factors(d))+1)

if __name__ == '__main__':
    main()
