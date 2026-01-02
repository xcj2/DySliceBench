N, A, B, C, D = [int(i) - 1 for i in input().strip().split(' ')]
N += 1
S = [c for c in input().strip()]
S += '#'


def check(current, dest):
  i = current + 1
  while True:
    if i >= dest:
      return True
    elif S[i] == '.':
      i = i + 1
    elif S[i + 1] == '.':
      i = i + 2
    else:
      return False


def passable():
  i = B
  while True:
    if i > D:
      return False
    elif S[i - 1] == '.' and S[i] == '.' and S[i + 1] == '.':
      return True
    else:
      i = i + 1


def main():
  if D > C:
    return check(B, D) and check(A, C)
  else:
    return passable() and check(A, C)


print('Yes' if main() else 'No')