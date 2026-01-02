import math
import itertools
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

def main():
    K=int(input())
    #l=[i for i in range(1,K+1)]
    ans=0
    dp=[[[None for i in range(201)] for j in range(201)] for k in range(201)]

    for i in range(1,K+1):
        for j in range(1,K+1):
            for k in range(1,K+1):
                p=sorted([i,j,k])
                if dp[p[0]][p[1]][p[2]] == None:
                    tmp=gcd(i,j,k)
                    dp[p[0]][p[1]][p[2]] = tmp
                    ans+=tmp
                else:
                    ans+= dp[p[0]][p[1]][p[2]]
    print(ans)
    
if __name__ == '__main__':
    main()   