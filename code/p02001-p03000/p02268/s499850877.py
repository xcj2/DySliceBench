#coding: UTF-8
#@document_it

def document_it(func):
  def new_function(*args,**kwargs):
    print('Running function:', func.__name__)
    print('Positional arguments:', args)
    print('Kewword arguments:', kwargs)
    result = func(*args,**kwargs)
    print('Result:', result)
    return result
  return new_function

#@document_it
def bsearch(v,list,l=None):
  if l == 0 or list == []:
    return False
  if l==None:
    l = len(list)
  
  import math
  T = math.ceil(math.log2(l))
  t = 0
  wid = l
  offset = 0
  while t <= T:
    if wid == 0:
        return False
    pos = wid//2 + offset
    w = list[pos]
    if wid == 1:
        if v == w:
            return True
        else:
            return False
    else:
        if v == w:
            return True
        elif v < w:
            wid = wid//2
        else:
            wid = wid//2 - 1 + wid%2
            offset = pos + 1
    t+=1



def exe():
    n = int(input())
    S = list(map(int,input().split()))
    q = int(input())
    T = map(int,input().split())
    ans = 0

    for t in T:
        if bsearch(t,S,n):
            ans += 1

    print(ans)

if __name__ == '__main__':
    exe()
