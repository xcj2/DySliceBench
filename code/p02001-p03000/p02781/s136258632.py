n = int(input())
k = int(input())
m = n
l = []
while m > 0:
    l.append(m%10)
    m //= 10

try:
  n_ = n-(l[-1]*10**(len(l)-1))
  m_ = n_
  l_ = []
  while m_ > 0:
      l_.append(m_%10)
      m_ //= 10

  n__ = n_-(l_[-1]*10**(len(l_)-1))
  m__ = n__
  l__ = []
  while m__ > 0:
      l__.append(m__%10)
      m__ //= 10
except:
  pass
      
def d1(lst):
  ans = 0
  for num,i in enumerate(lst):
    if num != (len(lst)-1):
      ans += 9
    else:
      ans += i
  return ans

def d2(lst,lst_):
  ans = 0
  for num,i in enumerate(lst):
    if num != (len(lst)-1):
      ans += 81*num
    else:
      ans += (i-1)*9*num+d1(lst_)
  return ans

def d3(lst,lst_,lst__):
  ans = 0
  for num,i in enumerate(lst):
    if num != (len(lst)-1):
      ans += 729*(num-1)*num//2
    else:
      ans += (i-1)*81*(num-1)*num//2+d2(lst_,lst__)
  return ans

if k ==  1:
  print(d1(l))
if k ==  2:
  print(d2(l,l_))
if k ==  3:
  print(d3(l,l_,l__))