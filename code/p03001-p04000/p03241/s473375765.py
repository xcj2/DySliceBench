import itertools


def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct
def factorize_list(n):
    result = []
    for val,perm in factorize(n):
        result+= [val]*perm
    return result



def mul(args):
    r =1
    for v in args:
        r*= v
    return r

def getcomb(l):
    if len(l)==0:
        return [1]
    result = []
    v,perm = l[0]
    for i in range(perm+1):
        result+= [(v**i)*val for val in getcomb(l[1:])]
    return result


N,M=list(map(int,input().split()))
factorized = factorize(M)
result=1
for i in range(len(factorized)//2+1):
    for vals in getcomb(factorized):
        A= vals
        B= M//A
        #print(A,B,vals)
        if A>=N:
            result = max(B,result)
        if B>=N:
            result = max(A,result)


print(result)