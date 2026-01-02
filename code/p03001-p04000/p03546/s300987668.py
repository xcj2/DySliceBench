def cost(n,clist):
  for k in range(0,10):
    for i in range(0,10):
      for j in range(0,10):
        clist[i][j] = min(clist[i][j],clist[i][k]+clist[k][j])
  
  return clist[n][1]

def joisino(a,clist):
  note = [-1,0,-1,-1,-1,-1,-1,-1,-1,-1]
  answer = 0
  for raw in a:
    for number in raw:
      if number != -1:
        if note[number] == -1:
          note[number] = cost(number,clist)
        answer += note[number]
      
  return answer

def i_o():
  h, w = map(int,input().split(" "))
  i = 0 
  clist = []
  while i < 10:
    raw = list(map(int,input().split(" ")))
    clist.append(raw)
    i += 1
  a = []
  i = 1
  while i <= h:
    raw = list(map(int,input().split(" ")))
    a.append(raw)
    i += 1
  return h,w,clist,a

if __name__ == '__main__':
  h,w,clist,a = i_o()
  ans =joisino(a,clist)
  
  print(ans, flush=True)