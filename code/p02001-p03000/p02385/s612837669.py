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
d2=[0 for i in range(6)]
d1[:]=(int(x) for x in input().split())
d2[:]=(int(x) for x in input().split())

if d1[2]==d2[0]:
  d2=E(d2)
elif d1[2]==d2[1]:
  d2=N(d2)
  d2=E(d2)
elif d1[2]==d2[3]:
  d2=E(d2)
  d2=E(d2)
elif d1[2]==d2[4]:
  d2=S(d2)
  d2=E(d2)
elif d1[2]==d2[5]:
  d2=W(d2)
elif d1[2]!=d2[2]:
  print("No")
  exit()

if d1==d2:
  print("Yes")
  exit()

for i in range(3):
  d2=N(d2)
  if d1==d2:
    print("Yes")
    exit()

print("No")

  
