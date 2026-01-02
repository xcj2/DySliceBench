import sys
n = int(sys.stdin.readline())
b = 20000000
a = [None]*b
def getC(c):
    if c == "A": t = 1
    elif c == "C": t = 2
    elif c == "G": t = 3
    elif c == "T": t = 4
    return t
def getK(s):
  ret = 0
  for c in s:
    ret = ret*5 + getC(c)
  return ret
def hash1(key):
  return key % b
def hash2(key):
  return 1 + key % (b-1)
def find(key):
  #print(key,a)
  i = 0
  j = (hash1(key)+i*hash2(key))%b
  while a[j]:
    if a[j] == key:
      return True
    i += 1
    j = (hash1(key)+i*hash2(key))%b
  return False
def insert(key):
  i = 0
  j = (hash1(key)+i*hash2(key))%b
  while a[j]:
    i += 1
    j = (hash1(key)+i*hash2(key))%b
  if a[j] == None:
    a[j] = key
for i in range(n):
  q,s = sys.stdin.readline().split()
  if q[0]=="i":
    insert(getK(s))
  else:
    if find(getK(s)):
      print("yes")
    else:
      print("no")

