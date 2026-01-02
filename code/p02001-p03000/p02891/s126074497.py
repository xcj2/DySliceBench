from itertools import groupby

S = input()
K = int(input())
A = []
for s in S:
  A.append(s)

def cont(A):
  B = []
  b = 0
  for key, value in groupby(A):
    B.append([key, list(value)])
  for i in range(len(B)):
    b += len(B[i][1]) // 2
  return b

def plus1(A):
  plu1 = 0
  for i in range(1,len(A)):
    if A[0] == A[i]:
      plu1 += 1
    else:
      break
  return plu1

def plus2(A):
  plu2 = 0
  for j in range(1,len(A)):
    if A[0] == A[-j]:
      plu2 += 1
    else:
      break
  return plu2

X = len(S) - len(list(set(A)))
if len(list(set(A))) == 1:
  an = len(S)*K
  ans = an // 2
elif X == 0:
  ans = 0
elif A[0] != A[-1]:
  ans = cont(A) * K
else:
  if plus1(A)%2 == 0 and plus2(A)%2 == 1:
    ans = cont(A)*K + (K-1)
  else:
    ans = cont(A) * K
print(ans)