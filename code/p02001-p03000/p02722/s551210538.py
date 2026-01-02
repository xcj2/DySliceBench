import sys
from collections import deque
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

N = I()

l = divisor(N)
l = list(set(l))

cnt = 0
for x in l:
  if x == 1:
    continue
  num = N
  while num%x == 0:
    num //= x
  if num%x == 1:
    cnt += 1

l = []

k = divisor(N-1)
cnt += len(k) - 1
print(cnt)