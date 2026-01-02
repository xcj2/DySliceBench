import math
# Python3 program to compute LCM of  
# array elements modulo M 
MAX = 1000003
  
mod = 1000000007
  
prime = [0 for i in range(MAX)] 
  
max_map = dict() 
  
# function to return a^n 
def power(a, n): 
      
    if n == 0: 
        return 1
    p = power(a, n // 2) % mod 
    p = (p * p) % mod 
      
    if n & 1: 
        p = (p * a) % mod 
    return p 
  
# function to find the smallest prime 
# factors of numbers upto MAX 
def sieve(): 
    prime[0], prime[1] = 1, 1
    for i in range(2, MAX): 
        if prime[i] == 0: 
            for j in range(i * 2, MAX, i): 
                if prime[j] == 0: 
                    prime[j] = i 
            prime[i] = i 
  
# function to return the LCM modulo M 
def lcmModuloM(arr, n): 
      
    for i in range(n): 
        num = arr[i] 
          
        temp = dict() 
          
        # temp stores mapping of prime factors  
        # to its power for the current element 
        while num > 1: 
               
            # factor is the smallest prime 
            # factor of num 
            factor = prime[num] 
              
            # Increase count of factor in temp 
            if factor in temp.keys(): 
                temp[factor] += 1
            else: 
                temp[factor] = 1
                  
            # Reduce num by its prime factor 
            num = num // factor 
              
        for i in temp: 
            # store the higest power of every prime 
            # found till now in a new map max_map 
            if i in max_map.keys(): 
                max_map[i] = max(max_map[i], temp[i]) 
            else: 
                max_map[i] = temp[i] 
              
    ans = 1
      
    for i in max_map: 
          
        # LCM is product of primes to their 
        # higest powers modulo M 
        ans = (ans * power(i, max_map[i])) % mod 
    return ans 
  
# Driver code 
sieve()
n = int(input())
a = list(map(int, input().split()))
if len(a) == 1:
    print(1)
    exit()
mod = 10**9+7
lcm = lcmModuloM(a, len(a))
ans = 0
for i in a:
    ans+=pow(i, mod-2, mod)
    ans%=mod
ans*=lcm
ans%=mod
print(ans)