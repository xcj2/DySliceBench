def floorsqrt(x):
  max_ok = 0
  min_ng = x+1
  while min_ng-max_ok>1:
    tgt = (max_ok+min_ng)//2
    if tgt*tgt<=x:
      max_ok = tgt
    else:
      min_ng = tgt
  return max_ok

def K1(C, r):
  max_ok = 0
  min_ng = C
  while min_ng-max_ok>1:
    tgt = (max_ok+min_ng)//2
    if C-tgt>r+tgt*tgt:
      max_ok = tgt
    else:
      min_ng = tgt
  return max_ok

def K2(C, r):
  max_ok = 0
  min_ng = C
  while min_ng-max_ok>1:
    tgt = (max_ok+min_ng)//2
    if C-tgt>r+tgt*(tgt+1):
      max_ok = tgt
    else:
      min_ng = tgt
  return max_ok

Q = int(input())
for _ in range(Q):
  A, B = map(int, input().split())
  if A*B==1:
    print(0)
    continue
  if B<A: A,B = B,A
  
  C = floorsqrt(A*B-1)
  #print(A, B, C, C*C, A*B-1, C*C+2*C+1)
  
  # C:= floor(sqrt(AB-1))
  
  q = (A*B-1)//C
  r = (A*B-1)%C

  if q==C:
    # Case 1: (AB-1)//C == C ... r
    # a :    1 ... C     AB-1
    # b : AB-1     C ...    1
    #
    # (AB-1)//(C-k) == C+k ... r+k*k
    # K = max{k | C-k>r+k*k}
    K = K1(C, r)
    ans = 2*C-3 if B<=C+K else 2*C-2
    #print(K, B, C+K)
  
  elif q==C+1:
    # Case 2: (AB-1)//C == C+1 ... r
    # a :    1 ... C   C+1     AB-1
    # b : AB-1     C+1   C...     1
    #
    # (AB-1)//(C-k) == C+k+1 ... r+k*(k+1)
    # K = max{k | C-k>r+k*(k+1)}
    K = K2(C, r)
    ans = 2*C-2 if B<=C+K+1 else 2*C-1
 
  else:
    # Case 3: (AB-1)//C == C+2
    # a :    1 ... C   C+2     AB-1
    # b : AB-1     C+2   C...     1
    ans = 2*C if A==B else 2*C-1
    
  print(ans)