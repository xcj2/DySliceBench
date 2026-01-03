from math import sqrt

def factors(n):
    N = n
    prime_dict = {}
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            prime_dict[i] = 1
            n //= i
            while n % i == 0:
                prime_dict[i] += 1
                n //= i
        if n == 1:
            break
    if n != 1:
        prime_dict[n] = 1
    return prime_dict

def factorial(n):
    if n == 1:
        return 1
    else:
        prime_set,prime_dict = set(),{}
        for i in range(2,n+1):
            F = factors(i)
            for fa in F:
                if fa not in prime_set:
                    prime_set.add(fa)
                    prime_dict[fa] = F[fa]
                else:
                    prime_dict[fa] += F[fa]

        output,M = 1,10**9+7
        for pr in prime_dict:
            output *= (prime_dict[pr]+1)
            output %= M
        return output

def main():
    N = int(input())

    print(factorial(N))

if __name__ == "__main__":
    main()
