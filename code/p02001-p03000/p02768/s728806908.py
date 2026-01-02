def pow(x, n, mod):
  ans = 1
  while(n > 0):
    if(bin(n & 1) == bin(1)):
      ans = ans*x % mod
    x = x*x % mod
    n = n >> 1
  return ans

def kaijou_k(n, k, mod):
    a = 1
    for i in range(k, n+1):
        a *= i
        a %= mod
    return a %mod

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 +7
    allsum = pow(2, n, mod)-1
    abunbo = kaijou_k(n, n-a+1, mod)
    abunsi = kaijou_k(a, 1, mod)
    asum = abunbo * pow(abunsi, mod-2, mod) % mod
    bbunbo = kaijou_k(n, n-b+1, mod)
    bbunsi = kaijou_k(b, 1, mod)
    bsum = bbunbo * pow(bbunsi, mod-2, mod) % mod
    ans = (allsum - asum - bsum) % mod
    print(ans)

if __name__ == '__main__':
    main()
