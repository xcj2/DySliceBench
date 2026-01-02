import sys,math

def input():
    return sys.stdin.readline()[:-1]
def yakusuu(N):
    P = [1,N]
    for k in range(2,math.floor(math.sqrt(N))+1):
        if N % k == 0:
            P.append(k)
            P.append(N//k)
    return P
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def main():
    A, B = map(int,input().split())
    C = sorted(list(set(yakusuu(A))&set(yakusuu(B))))

    if len(C) == 1:
        print(1)
        exit(0)
    D = [1]
    for k in range(1,len(C)):
        f = 1
        for l in range(k):
            if gcd(C[k],C[l]) != 1:
                f = 0
                break
        if f == 1:
            D.append(C[k])
    print(len(D))


if __name__ == '__main__':
    main()
