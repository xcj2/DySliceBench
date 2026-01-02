import sys
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read 
input = sys.stdin.buffer.readline
def inputS(): return input().rstrip().decode()
readlines = sys.stdin.buffer.readlines 

from functools import reduce

def gcd(a, b):
  while b:
    a, b = b, a%b
  return a

def lcm(a, b):
  return a*b // gcd(a, b)

N, M = map(int, input().split())
A = list(map(int, input().split()))
# 2で割ったものに置き換え a -> a'
Ad = [a//2 for a in A]

# 各要素について、2で割り切れる回数が等しいかチェック
div2 = None
for a in Ad:
  cnt = 0
  while a%2 == 0:
    a //= 2
    cnt += 1
  if div2 is None:
    div2 = cnt
  elif div2 != cnt:
    print(0)
    exit()
    
# LCM
_lcm = reduce(lcm, Ad)
if _lcm > M:
  print(0)
  exit()
  
print((M//_lcm + 1) // 2)   # 切り上げ

