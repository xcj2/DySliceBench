X = int(input())

def sqrt(x):
    last_guess=x/2
    while True:
        guess=(last_guess+x/last_guess)/2
        if abs(guess-last_guess)<.000001:
            break
        last_guess=guess
    return guess

def is_prime(n):
    if n == 1: return False
    for k in range(2, int(sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

def next_prime(N): 
    if (N <= 1): 
        return 2
  
    prime = N 
    found = False
    while(not found): 
        prime = prime + 1
  
        if(is_prime(prime) == True): 
            found = True
  
    return prime 

if 1==X:
    print(2)
    exit(0)
print(next_prime(X-1)) 