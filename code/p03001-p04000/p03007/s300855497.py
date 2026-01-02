def all_positive(values):
  m = []
  x = values[0]

  for v in values[1:-1]:
    m.append((x, v))
    x = x - v

  m.append((values[-1], x))
  x = values[-1] - x

  return x, m


def all_negative(values):
  m = []
  x = values[-1]

  for v in values[:-1]:
    m.append((x, v))
    x = x - v

  return x, m


def run(values):
  m = []
  x1 = values[0]
  x2 = values[-1]

  for v in values[-2::-1]:
    if v < 0:
      break

    m.append((x1, v))
    x1 = x1 - v

  for v in values[1:]:
    if v >= 0:
      break

    m.append((x2, v))
    x2 = x2 - v

  m.append((x2, x1))

  return x2 - x1, m


def main():
  input()
  values = list(map(int, input().split()))
  values.sort()

  if values[1] >= 0:
    x, m = all_positive(values)
  elif values[-2] <= 0:
    x, m = all_negative(values)
  else:
    x, m = run(values)

  print(x)
  for v in m:
    print('{} {}'.format(*v))


if __name__ == '__main__':
  main()
