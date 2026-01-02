import math

def heikatu(A,B):

    
    c = math.gcd(A,B)

    return (A//c,B//c)
 
 
def pow_r(x, n,mod=10**9+7):
    """
    O(log n)
    """
    if n == 0:  # exit case
        return 1
    if n % 2 == 0:  # standard case ① n is even
        return pow_r((x ** 2)%1000000007 , n // 2) % mod
    else:  # standard case ② n is odd
        return (x * pow_r((x ** 2)%1000000007, (n - 1) // 2) % mod) % mod
 
 
 
def resolve():
    N = int(input())
 
    
    km = dict()
    kp = dict()
    zero = [0,0]
    zerozero = 0
    for i in range(N):
        A,B = map(int,input().split())
 
        if A == 0 and B == 0:
            zerozero+=1

            continue
        
        if A == 0:
            B = -abs(B)
        if B == 0:
            A = abs(A)

 
        if A <0:
            A *= -1
            B *= -1
        xx = heikatu(A,B)
 
 
 
        if B < 0:
            if not xx in km:
                km[xx]=0
            km[xx]+=1
        else:
            if not xx in kp:
                kp[xx]=0
            kp[xx]+=1

    ans = 1

    groups = []
    for (x,y),v in km.items():
        if (-y,x) in kp:
            groups.append((v,kp[(-y,x)]))
            del kp[(-y,x)]
        else:
            groups.append((v,0))

    for v in kp.values():
        groups.append((v,0))


    for i,j in groups:
        ans *= (pow_r(2,i)+pow_r(2,j)-1)%1000000007
        ans %= 1000000007



    print((ans+zerozero-1)%(10**9+7))       

resolve()