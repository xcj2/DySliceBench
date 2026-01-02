from collections import defaultdict,deque
import math
def gcd(a,b):
    return b if not a%b else gcd(b,a%b)
def lcm(a,b):
    return (a*b)//gcd(a,b)

def main():
    n = int(input())
    A=[int(i) for i in input().split()]
    res = 0
    m = 0
    l_g = [0,A[0]]
    r_g = [0,A[-1]]
    ind = 2
    for i in A[1:]:
        l_g.append(gcd(l_g[ind-1],i))
        ind += 1
    ind = 2
    for i in range(n-2,-1,-1):
        r_g.append(gcd(r_g[ind-1],A[i]))
        ind += 1
    r_g = r_g[::-1]
    r_g = r_g[1:]

    for i in range(len(r_g)):
        if(r_g[i]!=0 and l_g[i]!=0):
            res = max(res, gcd(r_g[i],l_g[i]))
        else:
            res = max(r_g[i],l_g[i],res)
    print(res)

if __name__ == '__main__':
    main()
