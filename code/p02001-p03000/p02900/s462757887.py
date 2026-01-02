def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

def primeFactrization(n):
    i = 2
    table = []
    while i*i <= n:
        if  n % i ==0:
            table.append(i)
            while n % i == 0:
                n /= i
        i += 1
    if n > 1:
        table.append(n)
    return table

a,b = map(int, input().split())
c = gcd(a,b)
d = primeFactrization(c)
print(len(d)+1)
