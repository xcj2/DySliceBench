import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

N,P=LI()
S=input()

if P == 2 or P == 5:
  res = 0
  for i in range(N):
    if int(S[i])%P == 0:
      res += i+1
  print(res)
else:
  RESTS=[0]*(P+1)
  RESTS[0] = 1
  POWS=[0]*(N+1)
  POWS[0]=1
  res = 0
  for i in range(N): POWS[i+1] = (POWS[i]*10)%P

  cur = 0
  for i in range(N):
    cur += (int(S[N-1-i])*POWS[i])
    cur %= P
    res += RESTS[cur]
    RESTS[cur] += 1
  print(res)  

