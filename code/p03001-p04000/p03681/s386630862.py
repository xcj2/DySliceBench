n,m=map(int,input().split())
mod=10**9+7

def factorial(num):
    x=1
    for i in range(num,0,-1):
        x = x *i % mod

    return x
        
def permutations(num,r):
    x=1
    cnt=0
    for i in range(num,0,-1):
        if cnt>r:
            break

        x = x*i %mod
        cnt+=1

    return x

def solve():
    if abs(m-n)>1:
        print(0)
        return
    
    dog=factorial(n)

    if n==m:
        monkey=permutations(m,m-1)*2 % mod
    else:
        monkey=factorial(m)
    
    ans=dog * monkey % mod
    print(ans)
    
if __name__ == "__main__":
     solve()
