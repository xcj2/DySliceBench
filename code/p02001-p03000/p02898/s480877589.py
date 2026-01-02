def ri(): return int(input())
def rli(): return list(map(int, input().split()))
def rls(): return list(map(str, input().split()))
def pl(a): print(" ".join(list(map(str, a))))
def ma():return map(int,input().split())
def nli(x):return [input for _ in range(x)]
def hukusuu(): 
  listA=[] #appendのために宣言が必要
  while True:
    try:listA.append(list(map(int,input().split())))
    except:break #または、quit(),os.exit()をして止める。
  return listA

n,k=ma()
h=rli()

from itertools import accumulate as acc 
import operator as op
import copy as cp
import math
from bisect import bisect_left as bisl
from bisect import bisect_right as bisr
def ifif(s):
  if s:print("Yes")
  else:print("No")

h.sort()
inde=bisl(h,k)
print(n-inde)  



