N, M = map(int, input().split())

m = M//N

# def prime_factors(n):
#     i = 2
#     factors = OrderedDict()
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             if i in factors:
#               factors[i] += 1
#             else:
#               factors[i] = 1
#     if n > 1:
#       if n in factors:
#         factors[n] += 1
#       else:
#         factors[n] = 1
#     return factors

def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def divisorize(fct):
    b, e = fct.pop()  # base, exponent
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]


def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base**exponent
    return a

if M == 1:
  print(1)
  exit()

fct = factorize(M)
current_n = 1

for div in divisorize(fct):
    n = num(div)
    if n <= m and current_n < n:
      current_n = n

print(current_n)

# for x in range(m, 0, -1):
#   if M % x == 0:
#     print(x)
#     break

