def A():
    temp = input().split()
    print(''.join(temp[::-1]))

def B():
    temp = [int(n) for n in input().split()]
    A = temp[0]
    B = temp[1]
    K = temp[2]
    to_minus = min(A, K)
    A -= to_minus
    K -= to_minus
    if K > 0:
        B -= min(B, K)
    print (A, B)

import math
def C():
    X = int(input())
    if X <= 2:
        print(2)
        return

    def isPrime(n):
        if n <= 3:
            return True
        if(n % 2 == 0 or n % 3 == 0): 
            return False
      
        for i in range(5,int(math.sqrt(n) + 1), 6):  
            if(n%i == 0 or n%(i + 2) == 0): 
                return False
        
        return True
    
    while True:
        if isPrime(X):
            print(X)
            return
        X += 1

C()