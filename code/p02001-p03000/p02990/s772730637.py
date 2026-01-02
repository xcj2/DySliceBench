N,K = map(int,input().split())
mod_num = 10**9+7

def mul(a,b):
    return ((a % mod_num) * (b % mod_num)) % mod_num

def power(x,y):
    if y==0:                 
        return 1     
    elif y==1:                    
        return x % mod_num
    elif y%2 == 0:
        return power(x, y//2)**2 % mod_num
    else:
        return power(x, y//2)**2 * x % mod_num
    
def div(a,b):
    return mul(a, power(b, mod_num-2))


ans = N-K+1
ans %= mod_num
print(ans)

for i in range(1,K):
    if N-K+1-i>0:
        ans = mul(ans,K-i)
        ans = mul(ans,N-K+1-i)
        ans = div(ans,i)
        ans = div(ans,i+1)
        print(ans)
    else:
        print(0)