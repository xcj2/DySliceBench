import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = 10 ** 15
from itertools import accumulate

def equal_l(cumsum,i):
    f = lambda j:abs(cumsum[i + 1] - 2*cumsum[j])
    l = 1
    r = i + 1
    while r - l > 1:
        mid = (l + r)//2
        if f(mid) - f(mid - 1) >= 0:
            r = mid
        else:
            l = mid
    #print('equeal_l:{0},{1}'.format(l,r))
    return cumsum[i + 1] - cumsum[l],cumsum[l]

def equal_r(cumsum,i,N):
    f = lambda j:abs(cumsum[-1] - cumsum[i + 1] - 2*(cumsum[j] - cumsum[i + 1]))
    l = i + 2
    r = N
    while r - l > 1:
        mid = (l + r)//2
        if f(mid) -  f(mid - 1) >= 0:
            r = mid
        else:
            l = mid
    #print('equeal_r:{0},{1}'.format(l,r))
    return  cumsum[-1] - cumsum[l],cumsum[l] - cumsum[i + 1]

def main():
    N = int(input())
    A = list(map(int,input().split()))
    cumsum = list(accumulate([0] + A))
    ans = INF
    for i in range(1,N - 2):
        a,b = equal_l(cumsum,i)
        c,d = equal_r(cumsum,i,N)
        ret = max(a,b,c,d) - min(a,b,c,d)
        ans = min(ans,ret)
    print(ans)
    
if __name__ == '__main__':
    main()
    
