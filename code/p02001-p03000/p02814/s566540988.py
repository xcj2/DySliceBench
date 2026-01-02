N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list()
for i in range(N):
  B.append(A[i]//2)

def gcd(x, y):
  while(x % y != 0 and y % x != 0):
    if(x > y):
      x = x % y
    else:
      y = y % x
  if(x > y):
    return y
  else:
    return x
      
def lcm(x, y):
  return x * y // gcd(x, y)

def divide2(p):
  if(p % 2 == 1):
    return 0
  else:
    return divide2(p//2)+1

X = 1
for i in range(N):
  X = lcm(X, B[i])
  if(X > M):
    print(0)
    exit()

for i in range(1, N):
  if(divide2(A[0]) != divide2(A[i])):
    print(0)
    exit()
    
print((M-X)//(2*X) + 1)