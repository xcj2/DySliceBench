import math
import sys
import random

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

def sieve_of_erastosthenes(num):
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = math.sqrt(num)

    for serial in range(3, num, 2):

        if serial >= sqrt:
            return input_list

        for s in range(serial ** 2, num, serial): 
            input_list[s] = False

input_list = sieve_of_erastosthenes(10**6+1)
prime_list = [i for i, b in enumerate(input_list) if b == True]

def factorization(n):
    arr = []
    temp = n
    for i in prime_list:
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append(i)
    if temp!=1:
        arr.append(temp)
    if arr==[]:
        arr.append(n)
    return arr
random.shuffle(a)
g = a[0]
arr = factorization(a[0])
used = set()
for i in arr:
    if i == 1: continue
    used.add(i)

# not coprimeか判定
for i in range(n-1):
    g = gcd(g, a[i+1])
if g > 1:
    print('not coprime')
    exit(0)

# pairwise coprimeか判定
used = [0] * (10**6+1)
pair = True
for _a in a:
    if _a == 1:
        continue
    if used[_a]:
        print('setwise coprime')
        exit(0)
    else:
        used[_a] = True

for p in prime_list:
    v = p
    cnt = 0
    while v < 10**6+1:
        if used[v]:
            cnt+=1
        v += p
    if cnt > 1:
        print('setwise coprime')
        exit(0)
print('pairwise coprime')
