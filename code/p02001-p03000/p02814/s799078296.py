import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
a = [int(i) for i in input().split()]

# 最大公約数
def gcd(a, b) :
    if b > a : 
        a, b = b, a
    
    while b != 0 :
        a, b = b, a % b
    return a
    
# 最小公倍数
def lcm(a, b) :
    return a * b // gcd(a, b)

def solve() :
  f = a[0]
  if N >= 2 :
    for i in range(1, N) :
      f = lcm(f, a[i])
      if f > M * 2 :
        return 0
      
  cnt = 0
  while a[0] % 2 == 0 :
    a[0] //= 2
    cnt += 1
  
  for i in range(1, N) :
    tmp = 0
    while a[i] % 2 == 0 :
      a[i] //= 2
      tmp += 1
    if tmp != cnt :
      return 0
      
  return int(M / f + 0.5)
      
print(solve())
