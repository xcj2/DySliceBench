# = int(input())
# = map(int, input().split())
# = list(map(int, input().split()))
# = list(input())
# = [tuple(map(int, input().split())) for _ in range(n)]

n = int(input())
p = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()

MOD = 10 ** 9 + 7

MAX = max(p) + 1

inv = [0]+[1]
for i in range(2,MAX + 1):
    inv += [inv[MOD % i] * (MOD - MOD // i) % MOD]

prime = [0 for i in range(MAX)]

max_map = dict()


# function to return a^n
def power(a, n):
    if n == 0:
        return 1
    p = power(a, n // 2) % MOD
    p = (p * p) % MOD

    if n & 1:
        p = (p * a) % MOD
    return p


# function to find the smallest prime
# factors of numbers upto MAX
def sieve():
    prime[0], prime[1] = 1, 1
    for i in range(2, MAX):
        if prime[i] == 0:
            for j in range(i * 2, MAX, i):
                if prime[j] == 0:
                    prime[j] = i
            prime[i] = i

        # function to return the LCM MODulo M


def lcmModuloM(arr, n):
    for i in range(n):
        num = arr[i]

        temp = dict()

        # temp stores mapping of prime factors
        # to its power for the current element
        while num > 1:

            # factor is the smallest prime
            # factor of num
            factor = prime[num]

            # Increase count of factor in temp
            if factor in temp.keys():
                temp[factor] += 1
            else:
                temp[factor] = 1

            # Reduce num by its prime factor
            num = num // factor

        for i in temp:
            # store the higest power of every prime
            # found till now in a new map max_map
            if i in max_map.keys():
                max_map[i] = max(max_map[i], temp[i])
            else:
                max_map[i] = temp[i]

    ans = 1

    for i in max_map:
        # LCM is product of primes to their
        # higest powers MODulo M
        ans = (ans * power(i, max_map[i])) % MOD
    return ans

sieve()
c = lcmModuloM(p, n)

ans = 0
for x in p:
    ans = (ans + c * inv[x]) % MOD

print(ans)