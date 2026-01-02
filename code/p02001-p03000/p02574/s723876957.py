import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
lst1 = list(map(int,readline().split()))

import math
#リスト l の最大公約数
def gcdlist(l):
    a = l[0]
    for i in range(len(l)):
        a = math.gcd(a,l[i])
        if a == 1:
            return 1
    return a

res = gcdlist(lst1)
if res != 1:
    print("not coprime")
    exit()

#nまでの素数のリスト
def eratosthenes(n): #必要な分だけ用意
    if n < 2: #1は素数ではない
        return []
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p: #limit=root(n)
            return prime + data #root(n)まで判定すれば、残りは全て素数であると言える
        prime.append(p)
        data = [e for e in data if e % p != 0] #エラトステネスのふるい
"""素因数分解"""
def get_prime(n):
    b = 2
    fct = []
    while b*b <= n:
        while n % b == 0:
            n //= b
            if not b in fct:
                fct.append(b)
        b += 1
    if n > 1:
        fct.append(n)
    return fct
prime = eratosthenes(10**6)
prime_arr = [0]*10**6
for i in prime:
    prime_arr[i] = 1

for i in lst1:
    if prime_arr[i] == 1:
        prime_arr[i] = -1
    elif prime_arr[i] == -1:
        print("setwise coprime")
        exit()
    else:
        ret = get_prime(i)
        for i in ret:
            if prime_arr[i] == 1:
                prime_arr[i] = -1
            else:
                print("setwise coprime")
                exit()

print("pairwise coprime")