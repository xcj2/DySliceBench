import sys

MAX = 999999

def is_prime(n):
  if n == 2:return True
  if n % 2 == 0:return False
  for i in range(3,int(n**0.5)+1,2):
    if n % i == 0:return False
  return True

def prime_list(n):
  result = []
  if n >= 2:result.append(2)
  for i in range(3,n+1,2):
    if is_prime(i):result.append(i)
  return result

L = prime_list(int(MAX**0.5))

def is_prime_2(n):
  a = int(n ** 0.5)
  for i in L:
    if i > a:return True
    if n % i == 0:return False
  return True

def prime_count(n):
  result = 0
  if n >= 2:result+=1
  for i in range(3,n+1,2):
    if is_prime_2(i):result+=1
  return result

L2 = prime_list(MAX)

def prime_count_2(n):
  for i,v in enumerate(L2):
    if v > n:return i
  return len(L2)

for n in sys.stdin:
  print(prime_count_2(int(n)))