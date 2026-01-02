# coding: UTF-8

#共通関数と演算
def pprint(numlist):
  print(" ".join(map(str,numlist)))
def greater(s,t):
  if s[1] > t[1]:
    return True
  else:
    return False
def equal(s,t):
  if s[1] == t[1]:
    return True
  else:
    return False
def wasStable(Ans,Initial,N):
  I = Initial.copy()
  for i in range(N-1):
    if equal(Ans[i],Ans[i+1]):
      for x in I:
        if equal(Ans[i],x):
          if(Ans[i][0] != x[0]):
            return False
          else:
            I.remove(x)
            break
  return True
  
#input
N = int(input())
A = input().split()
Initial = A.copy()
B = A.copy()

#バブルソート
count = 0
flag = True
while flag:
  flag = False
  j = N - 1
  while j >= 1:
    if greater(A[j-1],A[j]):
      v = A[j]
      A[j] = A[j-1]
      A[j-1] = v
      flag = True
      count += 1
    j -= 1
pprint(A)
print("Stable")

#選択ソート
count = 0
for i in range(N):
  j=i
  minj=i
  while j<= N-1:
    if greater(B[minj],B[j]):
      minj = j
    j += 1
  if i != minj:
    v=B[i]
    B[i]=B[minj]
    B[minj]=v
    count += 1
    
print(" ".join(map(str,B)))
if wasStable(B,Initial,N):
  ans = "Stable"
else:
  ans = "Not stable"
print(ans)

    

