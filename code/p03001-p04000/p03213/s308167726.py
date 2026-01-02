n = int(input())
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]] #n番目までの素数のリストを生成
prime = primes(100)
primeCount = [0 for i in range(25)]

def searchSingle():
    res = 0
    for i in range(len(primeCount)):
        if primeCount[i] >= 74:
            res += 1
    return res

def searchDouble():
    res = 0
    for i in range(len(primeCount)):
        for j in range(len(primeCount)):
            cnt_i = primeCount[i]
            cnt_j = primeCount[j]
            if cnt_i >= 14 and cnt_j >= 4 and i != j:
                res += 1
            if cnt_i >= 24 and cnt_j >= 2 and i != j:
                res += 1
    return res

def searchTriple():
  res=0
  for i in range(len(primeCount)):
    for j in range(len(primeCount)):
      for k in range(j+1,len(primeCount)):
        if primeCount[i] >=2 and primeCount[j] >=4 and primeCount[k] >=4 and i!=j and j!=k and i!=k:
          res+=1
  return res

for i in range(2, n+1):
    cnt=i
    for j in range(len(prime)):
        if cnt % prime[j] == 0:
            while cnt % prime[j] == 0:
                cnt//= prime[j]
                primeCount[j] += 1
print(searchSingle() + searchDouble() + searchTriple())