# -*- coding: utf-8 -*-

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def factorize(a):
    ret = set()
    i = 2
    while i * i < a:
        if a % i != 0:
            i += 1
        else:
            while a % i == 0:
                a //= i
                ret.add(i)
            i += 1
    if a != 1:
        ret.add(a)
    return ret

def main():
    A, B = map(int,input().split())
    ABgcd = gcd(A, B)
    ABfactor = factorize(ABgcd)
    Ans = len(ABfactor) + 1
    print(Ans)

if __name__ == "__main__":
    main()
