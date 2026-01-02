import sys

def is_center(x, y, P):
  H = [abs(x-p[0]) + abs(y-p[1]) + p[2] for p in P if p[2] != 0]
  return H


def center(C, P):
  for c in C:
    check = [p[2] == max(c[2] - abs(p[0] - c[0]) - abs(p[1] - c[1]), 0) for p in P]
    if all(check):
      return '{} {} {}'.format(c[0], c[1], c[2])

def main():
  input = sys.stdin.readline
  N = int(input())
  P = [[0, 0, 0] for _ in range(N)]

  for i in range(N):
    x, y, h = map(int, input().split())
    P[i][0], P[i][1], P[i][2] = x, y, h

  C = []
  for i in range(101):
    for j in range(101):
      H = is_center(i, j, P)
      if len(set(H)) == 1:
        C.append([i, j, H[0]])
  
  ans = center(C, P)
  print(ans)


if __name__ == '__main__':
  main()