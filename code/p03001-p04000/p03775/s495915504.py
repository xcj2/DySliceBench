import math

# n以下の素数を列挙
def Primes(n):
    Prime = []
    Table = list(range(2, n+1))
    for k in range(2, int(math.sqrt(n))+1):
        if k == Table[0]:
            Prime.append(Table[0])
            Table = [i for i in Table if i % k]
    return Prime + Table if n >= 2 else []


# 素因数分解
def PrimeDecomp(m):
    n = m
    Dict = {}
    for p in Primes(int(math.sqrt(m))):
        for _ in range(1, m):
            if n % p == 0:
                n //= p
                Dict.setdefault(p, 0)
                Dict[p] += 1
            else:
                break
    if n > 1:
        Dict[n] = 1
    return Dict


# 約数列挙
def Divisors(m):
    Divisor = [1]
    for p in PrimeDecomp(m).keys():
        Table = []
        for j in range(PrimeDecomp(m)[p]+1):
            Table.extend([d*p**j for d in Divisor])
        Divisor = Table
    return sorted(Divisor)


Div = Divisors(int(input()))
print(len(str(Div[len(Div)//2])))
