table_prime_numbers = [True for _ in range(10 ** 5)]
table_2017_numbers = [False for _ in range(10 ** 5)]
table_2017_numbers_acm = [0 for _ in range(10 ** 5)]

def init_tables():
  table_prime_numbers[0] = table_prime_numbers[1] = False
  for i in range(2, 10 ** 5):
    if table_prime_numbers[i]:
      for j in range(i * 2, 10 ** 5, i):
        table_prime_numbers[j] = False
        
  for i in range(2, 10 ** 5):
    if table_prime_numbers[i]:
      if (i * 2 - 1 < 10 ** 5) and table_prime_numbers[i * 2 - 1]:
        table_2017_numbers[i * 2 - 1] = True
  
  for i in range(2, 10 ** 5):
    table_2017_numbers_acm[i] = table_2017_numbers_acm[i - 1] + int(table_2017_numbers[i])
      
  return

def cumul(n):
  return table_2017_numbers_acm[n]

def result(l, r):
  return cumul(r) - cumul(l - 1)

def main():
  q = int(input())
  
  for _ in range(q):
    l, r = map(int, input().split())
    print(result(l, r))

  return

if __name__ == "__main__":
  init_tables()
  main()
