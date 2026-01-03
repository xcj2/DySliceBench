def strip_left(str):
  if len(str) == 1:
    return ""
  else:
    return str[1:]

def role(str):
  if len(str) == 0:
    return 'z'
  else:
    return str[0].upper()


def solve(a,b,c):
  p = 'A'
  sa = a
  sb = b
  sc = c
  while True:
    if p == 'A':
      next_p = role(sa)
      sa = strip_left(sa)
      if next_p == 'z':
        return 'A'
      p = next_p
    elif p == 'B':
      next_p = role(sb)
      sb = strip_left(sb)
      if next_p == 'z':
        return 'B'
      p = next_p
    else:
      next_p = role(sc)
      sc = strip_left(sc)
      if next_p == 'z':
        return 'C'
      p = next_p

if __name__ == "__main__":
  a,b,c = [input() for _ in range(3)]
  print(solve(a,b,c))
