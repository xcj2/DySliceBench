import sys
INPUT = sys.stdin.readline

def SINGLE_INT(): return int(INPUT())
def MULTIPLE_INT_LIST(): return list(map(int, INPUT().split()))
def MULTIPLE_INT_MAP(): return map(int, INPUT().split())
def SINGLE_STRING(): return INPUT()
def MULTIPLE_STRING(): return INPUT().split()

MOD = 10 ** 9 + 7

N, M = MULTIPLE_INT_MAP()

floors = [0] * (N + 1)
floors[0] = 1
floors[1] = 1

for _ in range(M):
    floors[SINGLE_INT()] = -1

for i in range(2, N+1):

    if floors[i] == -1:
        continue

    if floors[i-2] == floors[i-1] == -1:
        floors[-1] = 0
        break

    if floors[i-2] > 0:
        floors[i] += floors[i-2]
    if floors[i-1] > 0:
        floors[i] += floors[i-1]

    floors[i] %= MOD

print(floors[-1])
