#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
  read_all = [tuple(map(int, input().split())) for _ in range(N)]
  return map(list,zip(*read_all))

#################

def make_divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
    if i != n // i:
      divisors.append(n//i)

  divisors.sort(reverse=True)
  return divisors

N,K = II()
A = III()

sumA = sum(A)
kouho = make_divisors(sumA)

for i in kouho:
  if sumA%i != 0:
    continue
  r = [0]*N
  for j in range(N):
    r[j] = A[j]%i
  sumr = sum(r)
  if sumr%i != 0:
    continue
  r.sort(reverse=True)
  num = 0
  for k in range(sumr//i):
    num += i-r[k]
  if num <= K:
    print(i)
    exit()