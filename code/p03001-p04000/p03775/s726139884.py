import math

N = int(input())
 
def divisor(N):
    '''
    create divisor_list < sqrt(N) from natural number
    '''
    divisor_list = []
    
    for num in range(1, math.ceil(math.sqrt(N)) + 1):
        if N % num == 0:
            divisor_list.append(num)
    
    return divisor_list
    
def F(A, B):
    return max(len(str(A)), len(str(B)))
  
def minimumF(N):
    factoring_list = divisor(N)
    
    candidate_list = []
    
    for A in factoring_list:
        B = N // A
        candidate_list.append(F(A, B))
        
    return min(candidate_list)
  
print(minimumF(N))