S = int(input())
import math

K = 10**9+7

def inverse_factorial(m):
    invs = [1,1]
    for i in range(2,m+1):
        t = invs[K % i] * (K // i)
        invs.append((-t) % K)
    return invs[1:]

def prod_mod_K(a_list):
    res = 1
    for a in a_list:
        res *= a
        res = res % K
    return res


def comb_mod_K(N,l):
    if l<N/2:
        den_seq = inverse_factorial(l)
        num_seq = [N,N-l+1]
    else:
        den_seq = inverse_factorial(N-l)
        num_seq = [N,l+1]
    num_seq = list(range(num_seq[1], num_seq[0]+1))
    res = prod_mod_K(num_seq) * prod_mod_K(den_seq)
    return res % K


l_max = int(S/3)
res = 0
for l in range(1,l_max+1):
    res += comb_mod_K(S-2*l-1,l-1)
print(res % K)
