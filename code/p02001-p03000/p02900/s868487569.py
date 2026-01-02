A, B = map(int, input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1
 
def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

cmlist = sorted(list(set(divisor(A)) & set(divisor(B))))
res = []
for cm1 in cmlist:
  can_append = True
  for cm2 in res:
    if not coprime(cm1, cm2):
      can_append = False
      continue
  if can_append:
    res.append(cm1)
print(len(res))