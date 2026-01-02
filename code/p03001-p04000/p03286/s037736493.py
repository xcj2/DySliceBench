def ip():
    return int(input())
    
def ipp():
    return map(int,input().split())
    
def sar():
    return list(ipp())
    
def pars(a):
    print(''.join(list(map(str, a))))
    print('\r')
    
def parl(a):
    print('\r'.join(list(map(str, a))))
    print('\r')
    
#template ends   

if __name__=='__main__':
    T=1
    #T=int(input().strip())
    for _ in range(T):
        n = ip()
        k = []
        if n==0:
            print(0)
        i = 0
        while n is not 0:
            k.append((n%(-2)))
            n = n//(-2)
            if (k[-1] == -1):
                k[-1] = 1
                n+=1
            i+=1
        k = k[::-1]
        pars(k)