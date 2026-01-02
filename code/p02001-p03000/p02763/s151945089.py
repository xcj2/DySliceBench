#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

class SegmentTree:
  __slots__ = ['ide','n','seg','segfunc']

  def __init__(self,size,func,element):
    self.segfunc = func
    self.ide = element
    # self.size = sizeを超える最小の2冪の数
    self.n = 2 ** (n-1).bit_length()
    # 全てのnodeの数は(2*n-1)個
    # 上にn-1個,最下段にn個
    self.seg = [self.ide] * (2*self.n-1)

  def apply(self,array):
    arraysize = len(array)
    # 配列埋め込み
    for i in range(arraysize):
      self.seg[self.n-1+i] = array[i]
    # 上にあげる
    for i in range(self.n-2,-1,-1):
      self.seg[i] = self.segfunc(self.seg[2*i+1],self.seg[2*i+2])

  def update(self,k,x):
    k += self.n -1
    self.seg[k] = x
    while k:
      k = (k-1)//2
      self.seg[k] = self.segfunc(self.seg[2*k+1],self.seg[2*k+2])

  def notrec(self,l,r):
    # 半開区間[l,r)
    l += self.n-1; r += self.n-1
    vl = vr = self.ide
    while l < r:
      if l & 1 == 0:
        vl = self.segfunc(vl,self.seg[l])
        l += 1
      if r & 1 == 0:
        vr = self.segfunc(vr,self.seg[r-1])
      l = (l-1)//2; r = (r-1)//2
    return self.segfunc(vl,vr)

def makebin(s):
  k = ord(s)-ord("a")
  # print(1<<k,k)
  return 1 << k

def segfunc(a,b):
  return a | b

def out(n):
  count = 0
  while n:
    if n & 1 == 1:
      print(chr(ord("a")+count))
    n//=2
    count += 1

n = int(input())
st = SegmentTree(n,segfunc,0)
S = input()
for i,si in enumerate(S):
  st.update(i,makebin(si))
Q = int(input())
# print(st.seg)
# exit()
for _ in range(Q):
  typo,a,b = input().split()
  if typo == "1":
    st.update(int(a)-1,makebin(b))
  else:
    print(bin(st.notrec(int(a)-1,int(b)))[1:].count("1"))
