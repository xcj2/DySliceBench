#!/mnt/c/Users/moiki/bash/env/bin/python
N = int(input())
sosu = [2]
import math

for i in range(3,101):
    fl = True
    for j in sosu:
        if j > math.sqrt(i):
            break
        if i % j == 0:
            fl = False
            break
    if fl:
        sosu.append(i)
# print(sosu)

def getpow(n, x):
    if n >= x:
        return 1 + getpow(n/x, x) if n % x == 0 else 0
    else:
        return 0

has = {}
powlist = []


for i in range(1,N+1):
    for p in sosu:
        if p > i:
            break
        if i % p == 0:
            has[p] = 2 if not p in has else has[p] + getpow(i,p)
            # print("p: {}".format(p))


# print(has)


def f(primes, num):
    if num == 1:
        # print("\t end: {}".format(primes))
        return 1
    else:
        sum = 0
        for e,p in enumerate(primes.keys()):
            for i in range(3, primes[p]+1):
                if num // i >= 1 and num % i == 0:
                    prime2 = primes.copy()
                    try:
                        # prime2[p] = prime2[p] - i
                        prime2[p] = 0
                    except:
                        print(prime2,e,p)
                        exit(1)
                    # print("num: {}, i: {},  {} => {}".format(num,i,primes,(prime2)))
                    sum += f(prime2, num//i)
        return sum
            

num75 = 0
num25 = 0
num15 = 0
num5  = 0
num3 = 0
# primes = has
primes = []
for p in has:
    primes.append(has[p])
def num(m):
    return len(
        list(
            filter(
                lambda x: 
                    x >=  m, primes
            )
        )
    )
    
# print(num(5), num(3), list(filter(lambda x: x >= 3, primes)))
# sum = f(has, 75)
# print(sum // 6)
sum = num(75) + num(25) * (num(3)-1) + num(15) * (num(5) - 1) + num(5) * (num(5)-1) * (num(3)-2) // 2
print(sum)






