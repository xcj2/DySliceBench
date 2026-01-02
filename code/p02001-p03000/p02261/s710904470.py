from sys import stdin
from copy import deepcopy

N = int(stdin.readline().rstrip())
C = [x for x in stdin.readline().rstrip().split()]

def sortBubble(C, N):
    c = deepcopy(C)
    for i in range(N):
        for j in range(N-1, i, -1):
            if c[j][1] < c[j-1][1]:
                c[j], c[j-1] = c[j-1], c[j]

    return c

def sortSelect(C, N):
    c = deepcopy(C)
    for i in range(N):
        minj = i
        for j in range(i, N):
            if c[j][1] < c[minj][1]:
                minj = j

        if i != minj:
            c[i], c[minj] = c[minj], c[i]

    return c

def isStable(Cin, Cout):
    stable = sortBubble(Cin, len(Cin))
    if len(stable) != len(Cout):
        return False
    else:
        for i in range(len(Cin)):
            if Cout[i][0] != stable[i][0]:
                return False
        else:
            return True
            
def output(C, N, *f):
    for fn in f:
        sortedC = fn(C, N)
        print(*sortedC)
        if isStable(C, sortedC):
            print("Stable")
        else:
            print("Not stable")

output(C, N, sortBubble, sortSelect)
