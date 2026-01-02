import math
import functools

law = 10 ** 9 + 7
def mul_mod(x, y):
  return x * y % law

def prod_mod(seq):
  return functools.reduce(mul_mod, seq, 1)
#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m
  
def comb(n, k):
  return prod_mod(i for i in range(n - k + 1, n + 1)) * mod_inv(prod_mod(i for i in range(1, k + 1)), law) % law

if __name__ == "__main__":
  
  x, y = sorted(map(int, input().split()), reverse=True)
  
  if (x + y) % 3 != 0:
    print(0)
  else:
    print(comb((x + y) // 3, x - (x + y) // 3))
