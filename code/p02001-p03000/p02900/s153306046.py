A, B = map(int, input().split())

#GCD
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

#List of divisors

def divisor(n):
    i = 1
    num = []
    while i * i <= n:
        if n%i == 0:
            num.append(i)
            num.append(n//i)
        i += 1
    num = list(set(num))
    return num


#Prime factorization
def factrization(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n >= 1:
        table.append(n)
    return table

n = gcd(A, B)
x = divisor(n)
count = 0
for i in x:
    prim_list = factrization(i)
    if len(prim_list) == 1:
        count += 1
print(count)