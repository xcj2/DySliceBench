def parse(s):
  ret = 0
  dic = {"m":1000, "c":100, "x":10, "i":1}
  while s:
    if s[0] in dic:
      ret += dic[s[0]]
      s = s[1:]
    else:
      ret += int(s[0]) * dic[s[1]]
      s = s[2:]
  return ret

def conv(n):
  ret = ""
  def func(ret, c, i):
    if i == 0:
      pass
    elif i == 1:
      ret += c
    else:
      ret += str(i) + c
    return ret
  a = n // 1000
  ret = func(ret, "m", a)
  n %= 1000
  b = n // 100
  ret = func(ret, "c", b)
  n %= 100
  c = n // 10
  ret = func(ret, "x", c)
  n %= 10
  ret = func(ret, "i", n)
  return ret

n = int(input())
for _ in range(n):
  s1, s2 = input().split()
  print(conv(parse(s1) + parse(s2)))
