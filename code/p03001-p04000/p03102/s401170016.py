#Reading input
def read_input():
  first_line = [int(item) for item in input().split()]
  n = first_line[0]
  m = first_line[1]
  c = first_line[2]
  b = [int(item) for item in input().split()]
  A =[]
  for i in range(n):
    A.append([int(item) for item in input().split()])
  return(n,m,c,b,A)

def validate(c,b,a):
  total = 0
  for i in range(len(a)):
    total += b[i]*a[i]
  if total + c>0:
    return 1
  else:
    return 0

def main():
  N,m,c,b,A = read_input()
  total = 0
  for n in range(N):
    total += validate(c,b,A[n])
  print(total)
if __name__ == '__main__':
  main()
  