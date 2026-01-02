from itertools import accumulate,chain,product
N,K = map(int,input().split())

V = tuple(map(int,input().split()))

av = tuple(chain((0,),accumulate(V)))


def left():
    for i in range(N+1):
        tmp = sorted(min(0, v) for v in V[:i])
        yield tuple(chain((0,), accumulate(tmp)))

left_cost = tuple(left())


def right():
    for i in reversed(range(N+1)):
        tmp = sorted(min(0, v) for v in V[i:])
        yield tuple(chain((0,), accumulate(tmp)))

right_cost = tuple(right())

def helper():
    for i in range(N+1):
        for j in range(N-i+1):
            d = K - i - j
            if d < 0:
                continue
            rev = av[i]+(av[N]-av[N-j])
            l,r = left_cost[i], right_cost[j]
            for k in range(d+1):
                yield rev - l[min(i,k)] - r[min(j,d-k)]
print(max(helper()))