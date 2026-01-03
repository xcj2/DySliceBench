import math
from functools import reduce
N=int(input())
MOD=10**9+7
'''
def all_multiple(a):
    return reduce(lambda a,b:a*b,a)
'''
def all_multiple_mod(a,m):
    return reduce(lambda a,b:((a%m)*(b%m))%m,a)

def is_prime(n):
    if n<=1 or (n!=2 and n%2==0):#nが１以下、あるいは、2ではない偶数
        return False
    elif 2<=n<=9:#n1が2以上９以下かつ2以外の偶数ではない
        return True
    else:#nが10以上の奇数〜√nまでの数で割り切れない場合は素数
        res=True
        for d in range(3,int(math.sqrt(n))+1,2):
            if n%d==0:
                res=False
                break
        return res
#print(is_prime(N))

'''
def is_prime(n):
    if n==1: return False
    for k in range(2,int(math.sqrt(n))+1):
        if n%k==0:
            return False
    return True
'''

A=[1]*(N+1)#indexと割られる数を合わせる
ans=1
for N_t in range(2,N+1):
    for num in range(1,N_t+1):
        if is_prime(num):
            cnt=0
            while N_t%num==0:
                N_t=N_t//num
                cnt+=1
            A[num]+=cnt 

print(all_multiple_mod(A,MOD)%MOD)

            
