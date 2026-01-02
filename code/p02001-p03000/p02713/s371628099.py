def gcd(a,b):
  while b!=0:
    a,b=b,a%b
  return a

def tri_gcd(a,b,c):
  return gcd(gcd(a,b),c)

def main():
  K = int(input())
  S = 0
  # a = b = c
  S_0 = 0
  for a in range(1,K+1):
    S_0 = S_0 + tri_gcd(a,a,a)
  S = S_0
  # a = b > c   
  S_1 = 0
  for a in range(1,K+1):
      for c in range(a+1,K+1):
          S_1 = S_1 + tri_gcd(a,a,c)
  S += 6*S_1

  # a > b > c   
  S_3 = 0
  for a in range(1,K+1):
      for b in range(a+1,K+1):
        for c in range(b+1,K+1):
            S_3 = S_3 + tri_gcd(a,b,c)
  S += S_3 * 6
  
  print(S)

  return 0
 
if __name__ == "__main__":
  main()