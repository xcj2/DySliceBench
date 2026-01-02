# 1. 最大公約数を求める(ユークリッドの互除法)
# 2. 最大公約数を素因数分解する。
# 3. 2.の結果に含まれる素因数の種類の数＋１が答え

def main():
  a, b = sorted(list(map(int, input().split())), reverse = True)
  while b != 0: a, b = b, a % b
  print(num_facto(a) + 1)  
  
def num_facto(n):
  ans = 0
  max_n = int(n ** 0.5) + 1
  is_prime = [True for x in range(max_n + 1)]
  is_prime[0], is_prime[1] = False, False
  for cursor in two_and_odds(max_n):
    if is_prime[cursor]:
      if n % cursor == 0:
        ans += 1
        while n % cursor == 0: n = n // cursor
      for i in range(cursor, max_n, cursor): is_prime[i] = False
  if n != 1: ans += 1
  return ans

def two_and_odds(max_n):
  if max_n >= 2: yield 2
  for i in range(3, max_n, 2): yield i
    
if __name__ == "__main__":
  main()
