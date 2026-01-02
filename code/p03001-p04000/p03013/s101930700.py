import sys
INPUT = sys.stdin.readline
MOD = 10 ** 9 + 7

def SINGLE_INT(): return int(INPUT())
def MULTIPLE_INT_LIST(): return list(map(int, INPUT().split()))
def MULTIPLE_INT_MAP(): return map(int, INPUT().split())
def SINGLE_STRING(): return INPUT()
def MULTIPLE_STRING(): return INPUT().split()

def solve(n, m):
    floors = [0] * (n + 1)
    floors[0] = 1
    floors[1] = 1

    last, current = 0,0

    for i in range(m):
        if i == 0:
            current = SINGLE_INT()
            floors[current] = -1

        else:
            last = current
            current = SINGLE_INT()
            floors[current] = -1
            if current == last + 1:
                return 0

    for i in range(2, n+1):
        if floors[i] == -1:
            continue
        else:
            if floors[i-2] > 0:
                floors[i] += floors[i-2]
            if floors[i-1] > 0:
                floors[i] += floors[i-1]

        floors[i] %= MOD

    return(floors[-1])


N, M = MULTIPLE_INT_MAP()

if N == 1:
    print(1)

elif N > 1:
    print(solve(N,M))