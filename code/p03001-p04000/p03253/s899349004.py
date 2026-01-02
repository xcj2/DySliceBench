import math
def fact(a,b):
    ans = 1
    while a != b:
        ans *= a
        a -= 1
    return ans
def nCr(n,r):
    return (fact(n,r)) // (math.factorial(n-r))
def nHr(n,r):
    return nCr(n+r-1, r-1)
def prime(n): # nまでの素数を列挙
    import math
    num_list = [i + 1 for i in range(2,n,2)]
    list_prime = [2]
    limit = math.sqrt(n)
    if n == 2:
        return list_prime
    else:
        while True:
            p = num_list[0]
            if p >= limit:
                return list_prime + num_list
            list_prime.append(p)
            num_list = [num for num in num_list if num % p != 0]

def primeFactorization(n):
    import math
    list_prime = prime(int(math.sqrt(n)))
    i = 0
    dict_pF = {}
    dict_primeFactorization = {}
    for pri in list_prime:
        dict_pF[pri] = 0
    while True:
        if n == 1:
            for key, value in dict_pF.items():
                if value != 0:
                    dict_primeFactorization[key] = value
            return dict_primeFactorization
        elif i >= len(list_prime):
            dict_pF[n] = 1
            for key, value in dict_pF.items():
                if value != 0:
                    dict_primeFactorization[key] = value
            return dict_primeFactorization
        p = list_prime[i]
        if n % p == 0:
            n //= p
            dict_pF[p] += 1
            continue
        else:
            i += 1

ans = 1
n,m = map(int, input().split())
if m == 1:
    ans = 1
else:
    for factor,degree in primeFactorization(m).items():
        ans *= (nHr(degree,n)) % (10**9+7)
        
print(ans % (10**9+7))
