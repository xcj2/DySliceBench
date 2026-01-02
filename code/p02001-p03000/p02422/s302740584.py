def defPrint(s,e):
  global str
  print(str[s:e+1])

def defReverse(s,e):
  global str
  strList = list(str)
  rStrList = strList[s:e+1][::-1]
  for i,x in enumerate(rStrList) :
    strList[s + i] = x
  str = "".join(strList)  
  
def defReplace(s,e,r):
  global str
  if s == 0:
    str = r + str[e+1:]
  else:
    str = str[0:s] + r + str[e+1:]

str = input()
q = int(input())

for i in range(q):
  cmd = list(input().split(" "))
  if cmd[0] == 'print' :
    defPrint(int(cmd[1]),int(cmd[2]))
  if cmd[0] == 'reverse' :
    defReverse(int(cmd[1]),int(cmd[2]))
  if cmd[0] == 'replace' :
    defReplace(int(cmd[1]),int(cmd[2]),cmd[3])
  
