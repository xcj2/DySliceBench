def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

A,B=map(int, input().split())
if (A==1)or(B==1)or(coprime(A,B)):
  print(1)
else:
  A=make_divisors(A)
  B=make_divisors(B)
  C=list(set(A)&set(B))
  C.sort(reverse=True)
  count=0
  for i in range(len(C)):
    for j in range(i+1,len(C)):
      if (C[j]!=1)and(C[i]%C[j]==0):
        count=count+1
        break
  print(len(C)-count)