import copy
import time


N = int(input())
As = list(map(int, input().split()))
As = [0] + As + [0]

t0 = time.time()

def dist(a, b):
    return abs(a - b)


dAs = [dist(As[i], As[i+1]) for i in range(N+1)]
sumdAs = sum(dAs)
# print(time.time()-t0, 'a')

def rem(i):
    ret = copy.deepcopy(dAs)
    print('copy', ret)
    ret[i] = dist(As[max(0, i-1)], As[i+1])
    print('rett', ret, i)
    ret = ret[:max(0, i-1)] + ret[i:]
    print('As', As)
    print('ret', ret)
    return ret

def calc(i):
    return sumdAs - dist(As[i], As[i-1]) - dist(As[i+1], As[i]) + dist(As[i+1], As[i-1])


for i in range(1, N+1):
    print(calc(i))
