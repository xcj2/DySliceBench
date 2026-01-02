N = int(input())
h = list(map(int, input().split()))

def zerosplit(l): # split by zero
  #print("zsp")
  mother = []
  child = []
  for e in l:
    if e != 0:
      child.append(e)
    elif e == 0 and len(child) != 0:
      mother.append(child)
      child = []
  if len(child) !=0:
    mother.append(child)
  return mother

def mizuyari(l): # decrease all elements by min(l)
  d = [0]*len(l)
  cnt1 = min(l)
  for i in range(len(l)):
    d[i] = l[i] - min(l)
  #print("mizuyari " + str(cnt1)+ " times")
  return [d,cnt1]
localcount = []
def mini(h): # mizuyari for splitted list
  l = zerosplit(h)
  #print(l)
  for e in l:
    #print(":in min: for"+ str(e))
    d,c = mizuyari(e)
    localcount.append(c)
    #print("localcnt " + str(localcount))    
    if len(d) != 0:
      mini(d)
  return sum(localcount)

print(mini(h))