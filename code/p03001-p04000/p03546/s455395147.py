def solve(inputstr):
  return inputstr

def rec_cost(x,acc,plist,clist):
  if x == 1:
    return acc
  else:
    minimum = -1
    for next in plist:
      nextplist = plist.copy()
      nextplist.remove(next)
      candidate = rec_cost(next,acc+clist[x][next],nextplist,clist)
      if minimum == -1:
        minimum = candidate
      elif candidate < minimum:
        minimum = candidate
    return minimum
      

def cost(n,clist):
 # print("invoked")
  plist = [0,1,2,3,4,5,6,7,8,9]
  plist.remove(n)
  return rec_cost(n,0,plist,clist)

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

def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n-1)
  
  
 
if __name__ == '__main__':
  h,w,clist,a = i_o()
  ans =joisino(a,clist)
  
  print(ans, flush=True)