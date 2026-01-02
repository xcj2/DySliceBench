# -*- coding: utf-8 -*-

################ DANGER ################
test = ""
test = \
"""

"""
########################################
test = list(reversed(test.strip().splitlines()))
if test:
    def input2():
        return test.pop()
else:
    def input2():
        return input()
########################################  
        
n = int(input2())

def primes(n):
    ps = [2]
    for odd in range(3, n + 1, 2):
        for p in ps:
            if odd % p == 0:
                break
            if p ** 2 > odd:
                ps.append(odd)
                break
    return ps


def isprime(n):
    last = int(n**.5)
    for m in primes(last):
        if n % m == 0:
            return False
    return True


if n in primes(n):
    print(n)
else:
    i = n
    while not isprime(i):
        i += 1
    print(i)


