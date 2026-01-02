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

def D():
    temp = [int(n) for n in input().split()]
    N = temp[0]
    K = temp[1]

    temp = [int(n) for n in input().split()]
    point_dict = {'r': temp[0], 's': temp[1], 'p': temp[2]}

    T = input()

    winning_rule = {'r': 'p', 's': 'r', 'p': 's'}

    ans = 0
    last_choice = ['' for i in range(K)]
    for i, c in enumerate(T):
        if i<K or last_choice[i%K] != winning_rule[c]:
            last_choice[i%K] = winning_rule[c]
            ans += point_dict[winning_rule[c]]
        else:
            last_choice[i%K] = None
    print(ans)

D()