import sys
sys.setrecursionlimit(1000000)

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def combination(n,r,q):
    if r==0:
        return 1

    return ((n*combination(n-1,r-1,q)%q)*modinv(r,q))%q

def _input():
    return list(map(int, input().split()))

def main():
    i=_input()
    x,y=i[0],i[1]
    if 2*y>=x and 2*x>=y and (2*y-x)%3==0 and (2*x-y)%3==0:
        n=(2*y-x)//3
        m=(2*x-y)//3
        print(int(combination(n+m,min(m,n),1000000007)))
    else:
        print(0)

if __name__ == "__main__":
    main()