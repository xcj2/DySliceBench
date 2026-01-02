
from math import gcd
def lcm(i, j):
  return i * j // gcd(i, j)
def main():
  while True:
    n = int(input())
    if not n: break
    lst = [[]]
    weight = [-1 for i in range(n + 1)]
    def setWeight(n):
      p, q, r, b = lst[n]
      if weight[n] != -1: pass
      elif r == 0 and b == 0:
        weight[n] = (p + q) // gcd(p, q)
      elif r == 0:
        setWeight(b)
        l = lcm(weight[b] * q, p)
        weight[n] = l // q + l // p
      elif b == 0:
        setWeight(r)
        l = lcm(weight[r] * p, q)
        weight[n] = l // p + l // q
      else:
        if weight[r] == -1: setWeight(r)
        if weight[b] == -1: setWeight(b)
        l = lcm(weight[r] * p, weight[b]  * q)
        weight[n] = l // p + l // q
    for i in range(n):
      lst.append(list(map(int,input().split())))
    for i in range(0, n):
      if weight[i + 1] == -1:
        setWeight(i + 1)
    print(max(weight))

if __name__ == '__main__':
  main()
