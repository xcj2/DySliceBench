S = input().rstrip()
Q = int(input().rstrip())


q = []
for n in range(Q):
  q.append(list(input().rstrip().split()))

#print(q)
def rev(olist):
  nlist  = olist[::-1]
  return nlist

def addhead(olist,ele):
  nlist = olist.insert(0,ele)
  return nlist
  
def addtail(olist,ele):
  nlist = olist.append(ele)
  return nlist

def rev2(flg):
  if flg == 0:
    flg = 1
  else:
    flg = 0
  return flg

def add(olist,ele,j,flg,head,tail):
  if j == '1' and flg == 0:
    head.insert(0,ele)
  elif j == '1' and flg == 1:
    tail.append(ele)
  elif j == '2' and flg == 0:
    tail.append(ele)
  elif j == '2' and flg == 1:
    head.insert(0,ele)
  
def add2(olist,ele,j,flg,head,tail):
  if j == '1' and flg == 0:
    head = ele + head
  elif j == '1' and flg == 1:
    tail = tail + ele
  elif j == '2' and flg == 0:
    tail = tail + ele
  elif j == '2' and flg == 1:
    head = ele + head
  return head,tail
flg = 0
#head = []
#tail = []
head=''
tail = ''
for n in range(Q):
  
  if q[n][0] == '1':
    flg = rev2(flg)
  
  else:
    head,tail = add2(S,q[n][2],q[n][1],flg,head,tail)


ans = head + S + tail

if flg == 1:
  ans1 = rev(list(ans))
  print(''.join(ans1))
else:
  print(ans)

