AA,BB,n=map(int,input().split())
CC=[]

if n==1:
    L=[1]
    l = sum(i >= AA for i in L)
    ll = sum(i > BB for i in L)
    print(l-ll)
    
else:
    def sample_code():
        fct = factorize(n)
        for div in divisorize(fct):
            C=(num(div))
            CC.append(C)


    def divisorize(fct):
        b, e = fct.pop()  # base, exponent
        pre_div = divisorize(fct) if fct else [[]]
        suf_div = [[(b, k)] for k in range(e + 1)]
        return [pre + suf for pre in pre_div for suf in suf_div]
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
    def num(fct):
        a = 1
        for base, exponent in fct:
            a = a * base**exponent
        return a
    if __name__ == '__main__':
        sample_code()
    CCC=sorted(CC)
    nnn = sum(i >= AA for i in CCC)
    NNN = sum(i > BB for i in CCC)
    print(nnn-NNN)
