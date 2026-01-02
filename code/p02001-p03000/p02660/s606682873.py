import math
from collections import Counter
def total(n):
    return int((-1 + math.sqrt(1 + 8 * n)) / 2); 
def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
  
def primeFactors(n): 
    tot = 0
    a = []
    while n % 2 == 0: 
        a.append(2)
        n = n / 2
          

    for i in range(3,int(math.sqrt(n))+1,2): 

        while n % i== 0: 
            a.append(i)
            n = n / i 

    if n > 2: 
        a.append(n)
    for i, j in Counter(a).items():
        tot+=total(j)
    return tot


def sol():
    n = int(input())
    if n == 1:
        print(0)
        return
    if isPrime(n):
        print(1)
        return

    print(primeFactors(n))
    
sol()
