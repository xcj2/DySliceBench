import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
S = [[0]*(m+1)] + [[0] + list(map(int, list(input().rstrip()))) for _ in range(n)]
B = [[0]*(m+1) for _ in range(n+1)]
U = [[0]*(m+1) for _ in range(n+1)]
L = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
  for j in range(1, m+1):
    B[i][j] = B[i-1][j] + B[i][j-1] - B[i-1][j-1] + S[i][j]
    U[i][j] = U[i-1][j] + U[i][j-1] - U[i-1][j-1] + U[i][j]
    L[i][j] = L[i-1][j] + L[i][j-1] - L[i-1][j-1] + L[i][j]
    if S[i][j]:
      U[i][j] += S[i-1][j]
      L[i][j] += S[i][j-1]
    
def calc_b(x1, y1, x2, y2):
  return B[x2][y2] - B[x1-1][y2] - B[x2][y1-1] + B[x1-1][y1-1]
def calc_u(x1, y1, x2, y2):
  return U[x2][y2] - U[x1][y2] - U[x2][y1-1] + U[x1][y1-1]
def calc_l(x1, y1, x2, y2):
  return L[x2][y2] - L[x1-1][y2] - L[x2][y1] + L[x1-1][y1]

for _ in range(q):
  x1, y1, x2, y2 = map(int, input().split())
  res = calc_b(x1, y1, x2, y2) - (calc_u(x1, y1, x2, y2) + calc_l(x1, y1, x2, y2))
  print(res)