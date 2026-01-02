# 1. 最大公約数を求める(ユークリッドの互除法)
# 2. 最大公約数を2と3以上の奇数で順次割っていくする（下から計算したら、素数判定は不要）
# 3. 2.の結果に含まれる数の種類の数＋１が答え

def main():
  a, b = sorted(list(map(int, input().split())), reverse = True) #aのほうを大きくする
  while b != 0: a, b = b, a % b #最大公約数を求める
  print(num_facto(a) + 1)  
  
def num_facto(n):
  ans = 0
  max_n = int(n ** 0.5) + 1
  
  if n == 1: return ans  
  for cursor in two_and_odds(max_n):
    if n % cursor == 0: ans += 1
    while n % cursor == 0: n = n // cursor
      
  if n != 1: ans += 1
  return ans

def two_and_odds(max_n):
  if max_n >= 2: yield 2
  for i in range(3, max_n, 2): yield i
    
if __name__ == "__main__":
  main()
