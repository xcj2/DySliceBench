import sys
from collections import defaultdict

sys.setrecursionlimit(500000)

def gcd(a,b):
    a,b = max(a,b),min(a,b)
    while a%b!=0:
        a,b = b,a%b
    return b

def frac(a,b):
    d = gcd(abs(a),abs(b))
    if a<0:
        a = -a
        b = -b
    return (a//d,b//d)

def inv(a,b):
    return frac(-b,a)

def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())

    vec = [list(map(int,input().split())) for i in range(N)]

    arg = defaultdict(int)
    zero = 0
    for v in vec:
        if v[0] == 0 and v[1] == 0:
            zero += 1
        elif v[1]==0:
            arg[float("inf")] += 1
            arg[0] += 0
        elif v[0]==0:
            arg[0] += 1
            arg[float("inf")] += 0
        else:
            arg[frac(v[0],v[1])] += 1
            arg[frac(-v[1],v[0])] += 0

    pair = []
    ll = lambda : False

    checked_list = defaultdict(ll)
    for key in arg:
        if not checked_list[key]:
            if key==0:
                pair.append([arg[0],arg[float("inf")]])
                checked_list[float("inf")] = True
            elif key==float("inf"):
                pair.append([arg[0],arg[float("inf")]])
                checked_list[0] = True

            else:
                #print(key)
                pair.append([arg[key],arg[inv(*key)]])
                #print(pair)
                checked_list[inv(*key)] = True

    mod = 1000000007

    ans = 1

    for p1,p2 in pair:
        ans *= pow(2,p1,mod) + pow(2,p2,mod) - 1
        ans %= mod

    ans += zero
    ans %= mod

    print((ans+mod-1)%mod)

if __name__ == '__main__':
    main()



