def power(x, a):
    if a == 0:
        return 1
    elif a == 1:
        return x
    elif a % 2 == 0:
        return power(x, a//2) **2 % mod
    else:
        return power(x, a//2) **2 * x % mod


def modinv(x):
    return power(x, mod-2)

def binomial_coefficients(n, k):
    numera = 1  
    denomi = 1  

    for i in range(k):
        numera *= n-i
        numera %= mod
        denomi *= i+1
        denomi %= mod
    return numera * modinv(denomi) % mod

X,Y=map(int,input().split())
mod=10**9 + 7
if Y<=2*X and Y>=0.5*X and (X+Y)%3==0:
  print(binomial_coefficients((X+Y)//3,((X+Y)//3)*2-X))
else:
  print(0)