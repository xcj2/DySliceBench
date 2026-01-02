import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

def sigma(func, frm, to):
    result = 0
    for i in range(frm, to+1):
        result += func(i)
    #print(result)

def f(x):
    return x

K = int(input())

#print(sigma(f,1,K))

#print(gcd(sigma(f,1,K),sigma(f,1,K),sigma(f,1,K)))

#sigma(sigma(sigma(gcd(), 1, K)))

#print(gcd(sigma(gcd,1,K),sigma(f(K),1,K),sigma(f(K),1,K)))

x = 0

#print()

for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            x += gcd(a, b, c)
            """print("a:",end="")
            print(a)
            print("b:",end="")
            print(b)
            print("c:",end="")
            print(c)"""

print(x)

#print(gcd(27,18,9))