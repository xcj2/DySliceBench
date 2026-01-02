import math

 

 
N,M = map(int,input().split())
S = input()
T = input()

pair = {N:S,M:T}


def lcd(n,m):
    return int(n * m / gcd(n,m))
def gcd(n,m):
    if n % m == 0:
        return m
    else:
        return gcd(m,n % m)
#    return int(m*n/math.gcd(n,m))
    
def prove(n,m):
    if gcd(n,m)==1:
        return lcd(n,m)
    global pair
    n_i = int(n/gcd(n,m))
    m_i = int(m/gcd(n,m))
    n_list = pair[n][::n_i]
    m_list = pair[m][::m_i]
#    print(c)
#    print(pair[m])
    if n_list[0:len(m_list)]==m_list:
        return lcd(n,m)
    else:
        return -1
n = max(pair.keys())
m = min(pair.keys())
if pair[N][0]!=pair[M][0]:
    print(-1)
elif N==M:
    if S==T:
        print(N)
    else:
        print(-1)
else:
    print(prove(n,m))

