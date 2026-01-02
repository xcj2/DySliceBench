def factorize(n, d):
  # if n == 0 or n == 1:
    # return []
    arr = []
    tmp = n
    while True:
      i = d[tmp]
      if i == 1:
        break
      #cnt=0
      while tmp%i==0:
        #cnt+=1
        tmp //= i
      arr.append(i)
    if tmp!=1:
      arr.append(tmp)
    if arr==[]:
      arr.append(n)
    return arr

def minimum_prime(n):
  # 試し割りをする際の最小の素数
  # エラトステネスの篩と同様の実装
    d = list(range(n+1))
    d[0] = 1
    for i in range(2, int(n**0.5) + 1):
        if d[i] != i:
          continue
        for j in range(i * 2, n + 1, i):
          if d[j] == j:
            d[j] = i
    return d  

def main():
  n = int(input())
  arr = list(map(int, input().split()))
  max_arr = max(arr)
  d = minimum_prime(max_arr)
  dp = [0]*(max_arr+1)
  
  
  searched = []
  for a in arr:
    if a != 1:
      primes = factorize(a, d)
      for p in primes:
        dp[p] += 1
  
  max_dp = max(dp)
  if max_dp < 2:
    print('pairwise coprime')
  elif max_dp == n:
    print('not coprime')
  else:
    print('setwise coprime')
    

main()