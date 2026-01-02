def solve():
  import sys
  import math

  sys.setrecursionlimit(10**7)
  readline=sys.stdin.readline

  def gcd(a,b):
    if a < b:
      a, b = b, a
    while b > 0:
      a, b = b, a % b
    return a

  
  def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
  

  a,b = map(int, input().split())

  max_gcd = gcd(a,b)

  ans = set(prime_factorize(max_gcd))

  print(len(ans)+1)

  
if __name__ == '__main__':
  solve()