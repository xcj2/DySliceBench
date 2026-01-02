n, a, b = map(int, input().split())
MOD = 10 ** 9 + 7

def power_func(a, n, mod):
  bi = bin(n)[2:]
  res = 1
  for i in range(len(bi)):
    res = (res * res) % mod
    if bi[i] == "1":
      res = (res * a) % mod
  return res

def modinv(a, mod):
    return pow(a, mod-2, mod)

def combination(n, r, mod):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

def main():
    ans = power_func(a=2, n=n, mod=MOD) - 1
    ans -= combination(n=n, r=a, mod=MOD)
    ans -= combination(n=n, r=b, mod=MOD)
    ans %= MOD
    print(ans)

if __name__ == "__main__":
    main()