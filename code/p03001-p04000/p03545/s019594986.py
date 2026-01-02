def calc(a,b,c,d,p,q,r):
  value = a
  list=[(p,b),(q,c),(r,d)]
  
  for el in list:
    op,x = el
    if op == 0:
      value += x
    elif op == 1:
      value -= x
    else:
      raise Exception("invalid argument")
  
  return value
  
def op(p):
  if p == 0:
    return '+'
  elif p == 1:
    return '-'
  else:
    raise Exception("invalid argument")
  
  

def solve(inputstr):
  a=int(inputstr[0])
  b=int(inputstr[1])
  c=int(inputstr[2])
  d=int(inputstr[3])
  
  ops=[0,1]
  for p in ops:
    for q in ops:
      for r in ops:
        if 7 == calc(a,b,c,d,p,q,r):
          return (inputstr[0] + op(p) + inputstr[1] + op(q) + inputstr[2] + op(r) + inputstr[3] + "=7")
    

  raise Exception("invalid argument")



if __name__ == '__main__':
  inputstr = input()
  ans = solve(inputstr)
  print(ans, flush=True)