import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
MOD=10**9+7
def divc(x,y) -> int: return -(-x//y)
def divf(x,y) -> int: return x//y
def enumerate_divs(n):
    """Return a tuple list of divisor of n"""
    return [(i,n//i) for i in range(1,int(n**0.5)+1) if n%i==0]
#======================================================#

def main():
    n = II()
    sumv = 0
    divs = enumerate_divs(n)
    for p,q in divs:
        if p!=1:
            if n//(p-1) == n%(p-1):
                sumv += p-1
        if q!=1:
            if n//(q-1) == n%(q-1):
                sumv += q-1
    print(sumv)

if __name__ == '__main__':
    main()