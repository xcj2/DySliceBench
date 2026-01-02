import math

 

 
N,M = map(int,input().split())
S = input()
T = input()


def lcd(n,m):
    return int(n * m / gcd(n,m))
def gcd(n,m):
    if n % m == 0:
        return m
    else:
        return gcd(m,n % m)
#    return int(m*n/math.gcd(n,m))
    
def prove(n,m):
    n_i = int(n/gcd(n,m))
    m_i = int(m/gcd(n,m))
    n_list,m_list=[],[]
    for i in range(gcd(n,m)):
        n_list += S[i*n_i]
        m_list += T[i*m_i]
#    print(c)
#    print(pair[m])
    if n_list==m_list:
        return lcd(n,m)
    else:
        return -1


print(prove(N,M))

