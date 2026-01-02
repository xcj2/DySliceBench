def dictionary_order(Xs, n):
  ascend = [i+1 for i in range(n)]

  order = 1
  for i, x in enumerate(Xs):
    order += ascend.index(x) * factorial(n-1-i)
    ascend.remove(x)
  return order

def factorial(n):
  out = 1
  for i in range(2, n+1):
    out *= i
  return out

def main():
  N = int(input())
  Ps = list(map(int, input().split()))
  Qs = list(map(int, input().split()))
  if Ps == Qs:
    print(0)
  else:
    P_order = dictionary_order(Ps, N)
    Q_order = dictionary_order(Qs, N)
    print(abs(P_order-Q_order))
  
if __name__ == '__main__':
  main()