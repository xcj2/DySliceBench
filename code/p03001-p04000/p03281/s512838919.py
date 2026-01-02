import math

#素数か(x>=2)
def prime_check(x): #x>=2
    if x==2:
        return True,2
    elif x%2==0:
        return False,2
    else:
        limit=int(math.sqrt(x))
        for factor in range(3,limit+1,2):
            if x%factor==0:
                return False,factor
        return True,x

#素因数分解(x>=2)
def prime_factorization(x): #x>=2
    factor_list=[]
    factor_dictionary={}
    factor_set=set()
    judge,factor=prime_check(x)
    while True:
        factor_list.append(factor)
        if factor in factor_set:
            factor_dictionary[factor]+=1
        else:
            factor_dictionary[factor]=1
            factor_set.add(factor)

        if judge:
            return factor_list,factor_dictionary,factor_set
            break
        else:
            x//=factor
            judge,factor=prime_check(x)

#素因数の個数(x>=2)
def total_number_of_factors(x):
    List,Dict,Set=prime_factorization(x)
    Total=1
    while Set:
        factor=Set.pop()
        Total*=Dict[factor]+1
    return Total


N=int(input())
ans=0
for i in range(1,N+1,2):
    if total_number_of_factors(i)==8:
        ans+=1
        
print(ans)


