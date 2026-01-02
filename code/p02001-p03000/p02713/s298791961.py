import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

MOD = 1000000007

def smax(a,b):
    if a>b:
        return a
    else:
        return b

def smin(a,b):
    if a<b:
        return a
    else:
        return b

def gcd(a,b):
    a,b = smax(a,b),smin(a,b)
    while a%b!=0:
        a,b = b,a%b
    return b

from collections import defaultdict

def main():
    K = int(readline())
    dd = defaultdict(int)

    for i in range(1,K+1):
        for j in range(1,K+1):
            dd[gcd(i,j)]+=1

    ans = 0
    for key in dd:
        for k in range(1,K+1):
            ans += dd[key]*gcd(key,k)
    print(ans)


if __name__ == '__main__':
    main()