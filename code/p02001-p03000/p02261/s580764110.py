def bubble(N,C):
  for i in range(N):
    for j in range(i+1,N)[::-1]:
      if C[j][1] < C[j-1][1]:
        _=C[j]
        C[j]=C[j-1]
        C[j-1]=_
  print(*C)

def selection(N,C):
  for i in range(N):
    minj=i
    for j in range(i,N):
      if C[minj][1] > C[j][1]:
        minj=j
    _=C[minj]
    C[minj]=C[i]
    C[i]=_
  print(*C)

def stable(A,C):
  result='Stable'
  for i in range(1,10):
    a=[j for j in A if j[1]==str(i)]
    c=[k for k in C if k[1]==str(i)]
    if a!=c:
      result='Not stable'
  print(result)

N=int(input())
C=list(input().split())
A=C[:]
bubble(N,C)
stable(A,C)
C=A[:]
selection(N,C)
stable(A,C)
