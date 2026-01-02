import sys
from math import factorial

def comb(a, b):
  return factorial(a) / (factorial(b) * factorial(a-b))


def f(A, a):
  if len(A) == 1:
    return A[0]
  
  if len(A) == 2:
    b1, b2 = A[0], A[1]
    if min(b1, a-b1) >= min(b2, a-b2):
      return b1
    else:
      return b2
  
  m = len(A) // 2
  b1, b2, b3 = A[m-1], A[m], A[m+1]
  c1, c2, c3 = min(b1, a-b1), min(b2, a-b2), min(b3, a-b3)
  c = max(c1, c2, c3)  
  
  if c2 == c:
    return b2
  elif c1 == c:
    return f(A[:m], a)
  else:
    return f(A[m+1:], a)


def main():
  input = sys.stdin.readline
  N = int(input())
  A = list(map(int, input().split()))
  A = sorted(A)
  ai = A[-1]
  A = A[:-1]
  aj = f(A, ai)
  print(ai, aj)


if __name__ == '__main__':
  main()