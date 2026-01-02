import math
ab = list(map(int,input().split()))
a = ab[0]
b = ab[1]
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
a_div = make_divisors(a)
b_div = make_divisors(b)

def is_prime(n):
    if n == 1: return True
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True
def primer(n):
    an = []
    for i in range(0,len(n)):
        if is_prime(n[i]) == True:
            an.append(n[i])
    return an
a_pri = primer(a_div)
b_pri = primer(b_div)
c =[]
for i in range(0,len(a_pri)):
    if b_pri.count(a_pri[i]) > 0:
        c.append(a_pri[i])
print(len(c))
