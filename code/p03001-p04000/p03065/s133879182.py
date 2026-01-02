def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
def prime_decomposition(n):
  i = 2
  d = {}
  while i * i <= n:
    while n % i == 0:
      n //= i
      if i not in d:
          d[i] = 0
      d[i] += 1
    i += 1
  if n > 1:
    if n not in d:
        d[n] = 1
  return d

def eratosthenes(n):
    if n < 2:
        return []
    prime = []
    limit = n**0.5
    numbers = [i for i in range(2,n+1)]
    while True:
        p = numbers[0]
        if limit <= p:
            return prime + numbers
        prime.append(p)
        numbers = [i for i in numbers if i%p != 0]
    return prime

N = int(input())
A = [int(input()) for i in range(N+1)]
g = abs(A[0])
for a in A:
     g = gcd(g,abs(a))
d = prime_decomposition(g)
ans = [p for p in d]

prime = eratosthenes(N+1)
A.reverse()
for p in prime:
    if A[0]%p != 0:
        continue
    for n in range(1,p):
        s = 0
        for k in range(int((N-n)/(p-1))+1):
            s += A[n+k*(p-1)]
            s %= p
        if s != 0:
            break
    if s == 0:
        ans.append(p)

ans = list(set(ans))
ans.sort()

for p in ans:
    print(p)
