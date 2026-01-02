#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = 0
A = [0]

def maxHeapify(A, i):
  l = i*2
  r = l+1
  if l <= n and A[l] > A[i]:
    largest = l
  else:
    largest = i
  if r <= n and A[r] > A[largest]:
    largest = r
  if largest != i:
    A[i],A[largest]=A[largest],A[i]
    maxHeapify(A,largest)

def insert(k):
  A.append(k)
  global n
  n += 1
  i = n
  while i > 1:
    #print(A)
    p = i>>1
    if A[p] > A[i]:
      break
    A[p],A[i] = A[i],A[p]
    i = p
  #buildMaxHeap(A)
  #maxHeapify(A, n)

def extract():
  ret = A[1]
  global n
  if 1 < n:
    A[1] = A.pop()
  else:
    A.pop()
  n -= 1
  maxHeapify(A,1)
  #buildMaxHeap(A)
  return ret

S = sys.stdin.readlines()
o = []
for s in S:
#while 1:
  if s[2]=="d":
    #print("\n".join(map(str,o)))
    print(*o,sep='\n')
    exit(0)
  elif s[0] == "i":
    insert(int(s[7:]))
  else:
    o.append(extract())
    #print(s,A)

