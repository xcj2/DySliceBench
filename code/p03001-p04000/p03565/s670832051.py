#
# Written by NoKnowledgeGG @YlePhan
# ('ω')
#
#import math
#mod = 10**9+7
#import itertools
#import fractions
#import numpy as np
#mod = 10**4 + 7
"""def kiri(n,m):
  r_ = n / m
  if (r_ - (n // m)) > 0:
    return (n//m) + 1
  else:
    return (n//m)"""

""" n! mod m 階乗
mod = 1e9 + 7
N = 10000000
fac = [0] * N
def ini():
  fac[0] = 1 % mod
  for i in range(1,N):
    fac[i] = fac[i-1] * i % mod"""

"""mod = 1e9+7
N = 10000000
pw = [0] * N
def ini(c):
  pw[0] = 1 % mod
  for i in range(1,N):
    pw[i] = pw[i-1] * c % mod"""

"""
def YEILD():
  yield 'one'
  yield 'two'
  yield 'three'
generator = YEILD()
print(next(generator))
print(next(generator))
print(next(generator))
"""
"""def gcd_(a,b):
  if b == 0:#結局はc,0の最大公約数はcなのに
    return a
  return gcd_(a,a % b) # a = p * b + q"""
"""def extgcd(a,b,x,y):
  d = a
  if b!=0:
    d = extgcd(b,a%b,y,x)
    y -= (a//b) * x
    print(x,y)
  else:
    x = 1
    y = 0
  return d"""
# 最大公約数 と 最小公倍数
"""def gcd(a,b):
  if b == 0:
    return a
  return gcd(b, a % b)
def lcm(a,b):
  g = gcd(a,b)
  return (a * b) // g"""

def readInts():
  return list(map(int,input().split()))
mod = 10**9 + 7

def main():
  import re
  #?tc????
  S = input().replace('?','.')
  T = input()
  #print(S)
  #.tc....
  #print(T)
  #coder
  # print(len(S) - len(T)) 7:5
  # 2
  for i in range(len(S) - len(T), -1,-1):
    # print(re.match(S[i:i+len(T)],T))
    # <_sre.SRE_Match object; span=(0, 5), match='coder'>
    # 後ろから、len(T)文まで見て、そこにTが入るかを検証
    # 入るなら Trueがかえる？
    if re.match(S[i:i+len(T)],T):
      #print(S) 
      S = S.replace('.','a')
      # すべてをaに置き換える(辞書順最初)
      print(S[:i] + T + S[i+len(T):])
      # i-1番目までSの部分、iからi+len(T)-1まではTを入れ（入れれることが確認できたから)
      # そして、i+len(T)番目から最後までSの部分を入れる
      exit()
  print('UNRESTORABLE')
if __name__ == '__main__':
  main()