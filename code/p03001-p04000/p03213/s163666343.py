n = int(input())
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
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