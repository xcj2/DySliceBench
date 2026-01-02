import math
n,m = map(int, input().split())
mod = 1000000007
fact = [1]*(n+10000+1)
rfact = [1]*(n+10000+1)
for i in range(n+10000):
    fact[i+1] = rr = ((i+1) * fact[i]) % mod
    rfact[i+1] = pow(rr, mod-2, mod)
def comb(N, K,mod):
    return fact[N] * rfact[K] * rfact[N-K] % mod
def make_prime_list_2(num):
    if num < 2:
        return []

    # 0のものは素数じゃないとする
    prime_list = [i for i in range(num + 1)]
    prime_list[1] = 0 # 1は素数ではない
    num_sqrt = math.sqrt(num)

    for prime in prime_list:
        if prime == 0:
            continue
        if prime > num_sqrt:
            break

        for non_prime in range(2 * prime, num, prime):
            prime_list[non_prime] = 0

    return [prime for prime in prime_list if prime != 0]
def prime_factorization_2(num):
    if num <= 1:
        print(1)
        exit()
        return False
    else:
        num_sqrt = math.floor(math.sqrt(num))
        prime_list = make_prime_list_2(num_sqrt)

        dict_counter = {}
        for prime in prime_list:
            while num % prime == 0:
                if prime in dict_counter:
                    dict_counter[prime] += 1
                else:
                    dict_counter[prime] = 1
                num //= prime
        if num != 1:
            if num in dict_counter:
                dict_counter[num] += 1
            else:
                dict_counter[num] = 1

        return dict_counter
x = prime_factorization_2(m)
x = list(x.values())
ans = 1
for i in x:
  ans*= comb(i+n-1,i,mod)
  ans %=mod
print(ans)