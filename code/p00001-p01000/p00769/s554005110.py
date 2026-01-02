from itertools import combinations

class Source:
  def __init__(self, S):
    self.S = S
    self.pos = 0

def peek(S):
  return S.S[S.pos] if S.pos < len(S.S) else a

def next(S):
  S.pos += 1
      
def expr(S):
  next(S)
  if peek(S) != '[':
    return num(S) // 2 + 1
    
  A = []
  while peek(S) != ']':
    A.append(expr(S))
    next(S)
  
  A.sort()

  return sum(A[:len(A) // 2 + 1])
  
def num(S):
  res = 0
  while '0' <= peek(S) <= '9':
    res = 10 * res + int(peek(S))
    next(S)
    
  return res
             
n = int(input())
for i in range(n):
  print(expr(Source(input())))

