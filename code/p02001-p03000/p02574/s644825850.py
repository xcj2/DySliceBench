import collections

def cin():  return list(map(int,input().split()))

N = cin()[0]
A = cin()

def gcd_(a, b):
    if a < b:  a, b = b, a
    if b == 0:  return a
    return gcd_(b, a % b)

def gcd(l):
    ans = l[0]
    for i in l:  ans = gcd_(ans, i)
    return ans

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:  f += 2
    if n != 1:  a.append(n)
    return a

flg = 0

s = [0 for _ in range(10 ** 6 + 5)]
for i in range(N):
    res = collections.Counter(prime_factorize(A[i])) # Counter({2: 4, 3: 1})
    keys = list(res.keys()) # [2, 3]
    length = len(keys)
    
    for i in range(length):
        num = keys[i] # 因数
        if s[num] == 1:
            flg = 1
            break
        s[num] += 1
        
if flg == 0:
    print("pairwise coprime")
else:
    if gcd(A) == 1:  print("setwise coprime")
    else:  print("not coprime")