def N(d1):
  t1=[0 for i in range(6)]
  t1[0]=d1[1]
  t1[1]=d1[5]
  t1[2]=d1[2]
  t1[3]=d1[3]
  t1[4]=d1[0]
  t1[5]=d1[4]
  return t1
def S(d1):
  t1=[0 for i in range(6)]
  t1[0]=d1[4]
  t1[1]=d1[0]
  t1[2]=d1[2]
  t1[3]=d1[3]
  t1[4]=d1[5]
  t1[5]=d1[1]
  return t1
def E(d1):
  t1=[0 for i in range(6)]
  t1[0]=d1[3]
  t1[1]=d1[1]
  t1[2]=d1[0]
  t1[3]=d1[5]
  t1[4]=d1[4]
  t1[5]=d1[2]
  return t1
def W(d1):
  t1=[0 for i in range(6)]
  t1[0]=d1[2]
  t1[1]=d1[1]
  t1[2]=d1[5]
  t1[3]=d1[0]
  t1[4]=d1[4]
  t1[5]=d1[3]
  return t1
d1=[0 for i in range(6)]
d1[:]=(int(x) for x in input().split())
q=int(input())

for i in range(q):
  t,f=(int(x) for x in input().split())
  if d1[1]==t:
    d1=N(d1)
  elif d1[2]==t:
    d1=W(d1)
  elif d1[3]==t:
    d1=E(d1)
  elif d1[4]==t:
    d1=S(d1)
  elif d1[5]==t:
    d1=N(d1)
    d1=N(d1)
  
  if d1[2]==f:
    d1=W(d1)
    d1=S(d1)
    d1=E(d1)
  elif d1[3]==f:
    d1=E(d1)
    d1=S(d1)
    d1=W(d1)
  elif d1[4]==f:
    d1=E(d1)
    d1=S(d1)
    d1=S(d1)
    d1=W(d1)
  print(d1[2])

    


