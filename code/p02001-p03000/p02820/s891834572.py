n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()
sco=[0]*n
ans=0

def sc(S):
  if S=='r':
    return p
  elif S=='s':
    return r
  else:
    return s

def bchk(i):
  score=0
  stnum=int(i//k)
  sta=int(i%k)
  if stnum==0:
    return sc(t[i])
  else:
    score=bnum=sc(t[sta])
    for j in range(1,stnum+1):
      if t[sta+j*k]==t[sta+(j-1)*k]:
        if bnum==0:
          bnum=sc(t[sta+j*k])
          score+=bnum
        else:
          bnum=0
          continue
      else:
        bnum=sc(t[sta+j*k])
        score+=bnum
    return score

def achk(i):
  score=0
  stnum=int(i//k)
  if stnum==0:
    return sc(t[i])
  else:
    score=bnum=sc(t[i])
    for j in range(1,stnum+1):
      if t[i-j*k]==t[i-(j-1)*k]:
        if bnum==0:
          bnum=sc(t[i-j*k])
          score+=bnum
        else:
          bnum=0
          continue
      else:
        bnum=sc(t[i-j*k])
        score+=bnum
    return score

for i in range(n):
  if sco[n-1-i]==0:
    ans+=max(achk(n-1-i),bchk(n-1-i))
    j=0
    while n-1-i-j*k>=0:
      sco[n-1-i-j*k]=1
      j+=1
print(ans)