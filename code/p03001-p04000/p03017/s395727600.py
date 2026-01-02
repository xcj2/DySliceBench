N, A, B, C, D = map(int, input().split())
S = input()

def max_stone(a, b):
  m = 0
  for j in range(a, b-1):
    if S[j] == S[j+1] == '#':
      return False
  
  return True
  
def reachable(b, d):
  n_sharp = 0
  n_dot = 0
  for j in range(b-1, d+1):
    s = S[j]
    if s=='.':
      n_dot += 1
      n_sharp = 0
    else:
      n_sharp += 1
      n_dot = 0
      
    if n_dot == 3:
      return True
    elif n_sharp == 2:
      return False
    
  return False

def reachable2(b, d):
  for k in range(b-1,d):
    if S[k] == S[k+1] == S[k+2] == ".":
      return True
  return False
  
if C < B:
  if max_stone(A-1, C) and max_stone(B-1, D):
    print('Yes')
  else:
    print('No')
elif B < C and C < D:
  if max_stone(A-1, C) and max_stone(B-1, D):
    print('Yes')
  else:
    print('No')
elif B < C and C > D:
  if reachable2(B-1, D-1) and max_stone(A-1, C) and max_stone(B-1, D):
    print('Yes')
  else:
    print('No')
