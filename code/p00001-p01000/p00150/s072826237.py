def primes(n):
  tf = [True] * (n + 1)
  tf[0] = tf[1] = False
  for i in range(2, int(n ** (1 / 2)) + 1):
    if tf[i]:
      for j in range(i ** 2, n + 1, i):
        tf[j] = False
  return [i for i in range(n + 1) if tf[i]]

def add_twin(prime_lst, twin_lst):
  prime_lst2 = prime_lst[1:]
  for x, y in zip(prime_lst, prime_lst2):
    if y - x == 2:
      twin_lst.append(y)

def search_twin(x, twin_lst):
  left = 0
  right = len(twin_lst)
  while left + 1 < right:
    mid = (left + right) // 2
    if twin_lst[mid] > x:
      right = mid
    elif twin_lst[mid] < x:
      left = mid
    else:
      return x
  return twin_lst[left]

prime_lst = primes(10000)
twin_lst = []
add_twin(prime_lst, twin_lst)

while True:
  n = int(input())
  if n == 0:
    break
  a = search_twin(n, twin_lst)
  print(a - 2, a)
