H, W, A, B = [int(x) for x in input().split()]

def formatMatrix(matrix):
  return "\n".join(["".join(x) for x in matrix])

def bitShift(matrix, n):
  for i in range(len(matrix)):
    matrix[i] = shift(matrix[i], n)
  return matrix

def shift(row, n):
  new = [0]*len(row)
  i = 0
  carry = False
  for x in row:
    ## If carry and last index not placed make 1
    if (i+n) > n:
      carry = True
    new[(i+n)%len(row)] = x
    i +=1 
  ### Alternative to this block of code would be in invert an entries in the matrix, ie turn 1's to 0's and vice versa
  if carry:
    for i in range((i+n)%len(row), len(row)):
      new[i] = '1'
  return new

def usualMatrix(n):
  i = 0
  x = []
  for a in range(n):
    x.append([])
    j = 0
    for y in range(n):
      if i == j:
        x[i].append('1')
      else:
        x[i].append('0')
      j += 1
    i += 1
  return x

def transpose(m):
  new = [[] for x in range(len(m[0])) ]
  for row in m:
    i = 0
    for entry in row:
      new[i].append(entry)
      i += 1
  return new

def thing(H,W,A,B):
  if H == W and A == 1 and B == 1:
    return usualMatrix(H)
  if H == 0 or W == 0:
    return -5
  if (B > H//2 or B < 0) or (A > W//2 or A < 0):
    return -1
  if B > A:
    a = thing1(W,H,B,A)
    if type(a) == int:
      return -1
    return transpose(a)  
  else:
    return thing1(H,W,A,B)
    
def thing1(H,W,A,B):
  matrix = [['1']*A+['0']*(W-A) for x in range(H)]
  part1 = bitShift(matrix[:B], A)
  part2 = matrix[B:]
  new_matrix = part1 + part2
  return new_matrix

matrix = thing(H,W,A,B)
if type(matrix) == int:
  print(-1)
else:
  print(formatMatrix(matrix))