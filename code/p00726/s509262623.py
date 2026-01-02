def string(s,i):
  l = 0
  while i < len(s) and s[i].isalpha():
    l += 1
    i += 1
  return i,l

def number(s,i):
  n = 0
  while i < len(s) and s[i].isdigit():
    n = n*10 + (ord(s[i])-ord('0'))
    i += 1
  return i,n

def block(s,i):
  if i < len(s) and s[i].isalpha():
    return string(s,i)
  else:
    i,n = number(s,i)
    if i < len(s) and s[i] == '(':
      i += 1
      sum = 0
      while i < len(s) and s[i] != ')':
        i,tmp = block(s,i)
        sum += tmp
      sum *= n
      i += 1
      return i,sum
    else:
      i,tmp = block(s,i)
      sum = tmp*n
      return i,sum

def find(s,i,j,p):
  if i == j:
    return 0
  k,l = block(s,i)
  if p < l:
    if i < j and s[i].isalpha():
      return s[i+p]
    else:
      i,n = number(s,i)
      if i < j and s[i] == '(':
        return find(s,i+1,k-1,p%(l//n))
      else:
        return find(s,i,k,p%(l//n))
  else:
    return find(s,k,j,p-l)

if __name__ == '__main__':
  while True:
    [s,p] = input().split()
    p = int(p)
    if s == "0" and p == 0:
      break
    print(find(s,0,len(s),p))

