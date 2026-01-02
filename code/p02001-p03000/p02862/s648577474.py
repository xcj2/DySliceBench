#
import sys
import math
import numpy as np
import itertools
# いくつか入力
x,y = (int(i) for i in input().split())  

MOD = 1000000007

if (x+y) % 3 != 0:
    print(0)
    exit()

if (x > y*2) or (y > x*2):
    print(0)
    exit()


a = x - (x+y) // 3
b = y - (x+y) // 3

upper=1
lower=1

for i in range(1,a+b+1,1):
    upper *= i
    upper %= MOD

for i in range(1,a+1,1):
    lower *= i
    lower %= MOD

for i in range(1,b+1,1):
    lower *= i
    lower %= MOD

# karimono
# https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6
def mul(a, b):
    return ((a % MOD) * (b % MOD)) % MOD

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % MOD
    elif y % 2 == 0 : return power(x, y//2)**2 % MOD
    else            : return power(x, y//2)**2 * x % MOD

def div(a, b):
    return mul(a, power(b, MOD-2))

answer = div(upper,lower)

print(answer)



