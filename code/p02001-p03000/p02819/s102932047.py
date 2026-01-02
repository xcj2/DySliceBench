import math
import random

def fermat(k):
    if k % 2 == 0 and k != 2:
      return False
            
    if pow(2, k-1, k) == 1:
      return True
    else:
      return False
def is_prime(n):
    if n == 2: return True
    if n == 1 or n & 1 == 0: return False

    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for k in range(100):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            return False

    return True    
def using_sqrt(k):  
    factor = 0
        
    # 2以外の偶数は素数ではないので無視する
    if k % 2 == 0 and k != 2:
        return False
        
    # 繰り返しの上限を対象の平方根にする
    for divisor in range(2, math.floor(math.sqrt(k))+1):
        if k % divisor == 0:
            factor += 1
                
    if factor == 0:
        return True
    else:
        return False
            
 
  
n=int(input())
while True:
  if fermat(n):
    if using_sqrt(n):
      print(n)
      break
  if is_prime(n):
    if using_sqrt(n):
      print(n)
      break    
  n+=1