from functools import reduce

# def gcd(a, b):
#   if (b == 0):
#     return a
#   return gcd(b, a % b)

# def lcm(a, b):
#   return a * b / gcd(a, b)

def lcm(a, b): 
    def gcd(a, b):  # a >= b
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    return a * b // gcd(a, b)

def main():
  n = int(input())
  li = []
  for i in range(n):
    inp = int(input())
    li.append(inp)

  ans = int(reduce((lambda x, y: lcm(x, y)), li))
  if ans > 1000000000000000000:
    ans = 1000000000000000000
  print(ans)

if __name__ == "__main__":
  main()