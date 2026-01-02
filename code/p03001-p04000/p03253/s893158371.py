N, M = [int(i) for i in input().split(' ')]
mod = pow(10, 9) + 7
def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NNN = (10**5) * 2
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range( 2, NNN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    c = 0
    while n % i == 0:
      n /= i
      c+=1
    if c!=0:
        table.append(c)
    i += 1
  if n > 1:
    table.append(1)
  return table

xxs = prime_decomposition(M)

result = 1
for xx in xxs:
    result = mul(result, cmb(xx+N-1,xx,mod))
print(result)
