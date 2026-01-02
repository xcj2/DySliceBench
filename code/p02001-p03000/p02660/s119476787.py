# coding: utf-8
import sys

stdin = sys.stdin
ns = lambda: stdin.readline().rstrip() # ignore trailing spaces
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
    

def cnt(n):
    x = int(-0.5 + pow(1+8*n,0.5)/2)
    if n < x*(x+1)//2:
        return x-1
    else:
        return x
    

def main():
    n = ni()
    ps = factorization(n)
    ans = 0
    for pi in ps:
        if pi[0] != 1:
            ans += cnt(pi[1])
    print(ans)
    return


if __name__ == '__main__':
    main()