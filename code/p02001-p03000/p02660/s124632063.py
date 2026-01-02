import math
from sys import stdin
input = stdin.readline


class Eratos:
  def __init__(self, n):

    self.is_prime = [True]*(n+1)
    self.is_prime[0] = False
    self.is_prime[1] = False
    self.primes = []

    # for i in range(2, int(math.sqrt(n))+1):
    for i in range(2, n):
      if self.is_prime[i]:
        self.primes.append(i)
        j = i + i
        while j <= n:
          self.is_prime[j] = False
          j += i

  def all(self):
    return self.primes


def main():
  N = int(input())

  MAX = 10**6
  primes = Eratos(MAX).all()

  cnt = 0
  for p in primes:
    if N < p: break
    e = 1
    while not(N % p**e):
      N //= (p**e)
      cnt += 1
      e += 1

  if N > MAX:
    for p in primes:
      while N % p == 0:
        N //= p
    if N > MAX:
      print(cnt+1)
    else:
      print(cnt)
  else:
    print(cnt)


if(__name__ == '__main__'):
  main()
