#######################################
import numpy as np
import math
import copy
import re
import sys
#sys.exit(0)

inf = float("inf")
prime = 1

def check_print(check_flag, text, end="\n"):
  if check_flag:
    print(text, end=end)

def c2i(x):
    if str.isdecimal(x):
        return int(x)
    else:
        return x

def cout(*args):
  arglist = []
  for arg in args:
    if hasattr(arg, "__iter__"):
      arglist.extend(arg)
    else:
      arglist.append(arg)
      
  arglist = list(map(str, arglist))
  print(" ".join(arglist))
  
def count2(num):
  count=0
  while num%2==0:
    num/=2
    count+=1
  return count

def ketasum(num):
  nums = [int(s) for s in str(num)]
  return sum(nums)

#math
def gcd(a, b): #最大公約数
  while b:
    a, b = b, a % b
  return a

def lcm(a, b): #最小公倍数
  return a * b // gcd (a, b)

def gcd3(lis): #最大公約数(3over)
  ans = lis[0]
  for li in lis:
    ans = gcd(ans,li)

def lcm3(lis): #最小公倍数(3over)
  ans = lis[0]
  for li in lis:
    ans = lcm(ans,li)

def divisor(n): #nの約数を全て求める
  i = 1
  table = []
  while i * i <= n:
    if n%i == 0:
      table.append(i)
      table.append(n//i)
    i += 1
  table = list(set(table))
  return table

def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table

def is_prime(n):
  for i in range(2, n + 1):
    if i * i > n:
      break
    if n % i == 0:
      return False
  return n != 1

#input stock
"""
n = int(input())

#list
a = map(int, input().split())
a,b = map(int, input().split())

d=[]
for i in range(n):
  d[i]=int(input())

#2dim-list
a = [list(map(int, input().split())) for i in range(n)]

s = input()
ss =  [int(si) for si in s]
"""

#processing stock
"""
a = sorted(a)
a = sorted(a, reverse=True)

"""

#regex
"""
pattern = ""
result = re.search(pattern, s)

result = re.fullmatch(pattern, s)

result = re.finditer(pattern, s)
for res in result:
    print res.group()   # 1回目: ca      2回目: ca   
    print res.start()   # 1回目: 0       2回目: 6      
    print res.end()     # 1回目: 2       2回目: 8      
    print res.span()    # 1回目: (0, 2)  2回目: (6, 8)
"""

#######################################
r = int(input())

print(3*r**2)



