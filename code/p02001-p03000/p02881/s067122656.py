# -*- coding: utf-8 -*-
import math
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

def findRoot(N):
    root = round(math.sqrt(N+1))
    return root

def main():
    N=int(input())  #数値入力 「N」だけの入力のとき
    for i in list(reversed(range(1, findRoot(N)+1))):
        a, b = divmod(N, i)
        if b == 0:
            c = N // a
            print(a+c-2)
            break
            

if __name__ == '__main__':
    main()