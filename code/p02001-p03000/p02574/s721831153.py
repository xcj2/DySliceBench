N = int(input())
A = [int(i) for i in input().split()]

def prime_factor(x) :
  ret = dict()
  if x % 2 == 0 :
    ret[2] = 0
    while x % 2 == 0 :
      x //= 2
      ret[2] += 1
          
  i = 3
  while i * i <= x :
    if x % i == 0 :
      ret[i] = 0
      
      while x % i == 0 :
        x //= i
        ret[i] += 1
    i += 2
      
  if x != 1 :
    ret[x] = 1
  
  return ret

def pairwise() :
  done = set()
  for a in A :
    for k in prime_factor(a).keys() :
      if not k in done :
        done.add(k)
      else :
        return False
  return True
    
def setwise() :
  done = set(prime_factor(A[0]).keys())
  for a in A[1:] :
    done &= set(prime_factor(a).keys())
    if len(done) == 0 :
      return True
  return False
  
if pairwise() :
  print('pairwise coprime')
elif setwise() :
  print('setwise coprime')
else :
  print('not coprime')