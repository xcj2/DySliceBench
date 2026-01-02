
def sRaw():
    return input().rstrip("\r")


def iRaw():
    return int(input())


def ssRaw():
    return input().split()


def isRaw():
    return list(map(int, ssRaw()))

INF = 1 << 29

DIV = (10**9) + 7

def mod_inv_prime(a, mod=DIV):
    return pow(a, mod-2, mod)

def mod_inv(a, b):
    r = a
    w = b
    u = 1
    v = 0
    while w != 0:
        t = r//w
        r -= t*w
        r, w = w, r
        u -= t*v
        u, v = v, u
    return (u % b+b) % b


def CONV_TBL(max,mod=DIV):
    fac,finv,inv = [0]*max, [0]*max, [0]*max
    fac[0]=fac[1]=1
    finv[0]=finv[1]=1
    inv[1]=1
    for i in range(2,max):
        fac[i] = fac[i-1]*i % mod
        inv[i] = mod -inv[mod%i] * (mod//i)%mod
        finv[i] = finv[i-1]*inv[i]%mod
    class CONV:
        def __init__(self):
            pass
        def ncr(self,n,k):
            if(n<k):
                return 0
            if(n<0 or k<0 ):
                return 0
            return fac[n]*(finv[k]*finv[n-k]%mod)%mod
    return CONV()



def main():
    N,K = isRaw()
    Hs = isRaw()
    Hs.sort()
    ans = 0
    for eidx in range(0,N-K):
        ans+=Hs[eidx]
    return ans


if __name__ == "__main__":
    print(main())
