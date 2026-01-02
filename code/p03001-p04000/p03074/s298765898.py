class BufInput:
  def __init__(self):
    self.save = False
    self.buf = None
  def read(self, save=False):
    if self.save:
      ret = self.buf
    else:
      try:
        ret = input()
      except EOFError as e:
      	ret = None
    self.save = save
    self.buf = ret
    return ret
    
  
bi = BufInput()
while bi.read(True):
  n, k = map(int, bi.read().split())
  s = bi.read().rstrip()

  def findEx(s, f, pos, notfound):
    pos = s.find(f, pos)
    if pos == -1:
      pos = notfound
    return pos

  ans = 0
  left = 0
  right = 0
  while right < n:
      if k > 0:
          right = findEx(s, '01', right, n-1) + 1
          k = k - 1
          right = findEx(s, '10', right, n-1) + 1
          ans = max(ans, right - left)
      else:
          left = findEx(s, '01', left, n-1) + 1
          k = k + 1

  print(ans)
