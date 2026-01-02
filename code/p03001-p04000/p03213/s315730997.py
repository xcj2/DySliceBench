
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(2,50): # prime > 50 never appear twice
    if is_prime(i):
        primes.append(i)

def make_zeroed():
    return [0] * len(primes)

factorized = []
factorized.append(make_zeroed())
for i in range(2, 101):
    lst = make_zeroed()
    for k, p in enumerate(primes):
        if i < p:
            break
        while i % p == 0:
            lst[k] += 1
            i = i // p
    factorized.append(lst)

sum_factorized = []
for i in range(1,101):
    lst = make_zeroed()
    for j in range(0, i):
        for k, f in enumerate(factorized[j]):
            lst[k] += f
    sum_factorized.append(lst)

def fact(n):
    a = 1
    for i in range(1,n+1):
        a *= i
    return a

def nCr(n,r):
    if r > n:
        return 0
    return fact(n) // fact(r) // fact(n - r)

def getelems(n):
    lst = sum_factorized[n-1]
    elems = {}
    elems[3] = len([x for x in lst if x >= 2])
    elems[5] = len([x for x in lst if x >= 4])
    elems[15] = len([x for x in lst if x >= 14])
    elems[25] = len([x for x in lst if x >= 24])
    elems[75] = len([x for x in lst if x >= 74])
    return elems

def solve(n):
    elems = getelems(n)
    ans = 0
    # 3 * 5 * 5
    ans += nCr(elems[5], 2) * nCr(elems[3] - 2, 1)
    # 5 * 15
    ans += nCr(elems[15], 1) * nCr(elems[5] - 1, 1)
    # 3 * 25
    ans += nCr(elems[25], 1) * nCr(elems[3] - 1, 1)
    # 75
    ans += nCr(elems[75], 1)
    return ans

answers = {}
for i in range(1,101):
    answers[i] = solve(i)

print(answers[int(input())])
