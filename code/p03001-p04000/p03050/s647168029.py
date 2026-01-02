import math
x = int(input())
if x == 1:
  print(0)
  exit()
  
d = math.ceil((x+1)**0.5)
def divisorize(fct):
    b, e = fct.pop()
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]
 
 
def factorize(n):
    fct = []
    b, e = 2, 0
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
 
 
def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base**exponent
    return a

ans = 0
fct = factorize(x)
for div in divisorize(fct):
    c = num(div)
    if d+1 <= c:
      ans += c-1
      
print(ans)
