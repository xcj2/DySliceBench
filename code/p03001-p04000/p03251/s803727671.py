from sys import stdin
def isWar_X(z, lst):
    for i in range(len(lst)):
        if lst[i] >= z:
            return True
    return False

def isWar_Y(z, lst):
    for i in range(len(lst)):
        if lst[i] < z:
            return True
    return False

def isWar(X, Y, xs, ys):
    for z in range(X+1, Y):
        if (not(isWar_X(z, xs)) and not(isWar_Y(z, ys))):
            return "No War"
    return "War"

N, M, X, Y = [int(x) for x in stdin.readline().rstrip().split()]
xs = [int(x) for x in stdin.readline().rstrip().split()]
ys = [int(x) for x in stdin.readline().rstrip().split()]
print(isWar(X,Y, xs, ys))
