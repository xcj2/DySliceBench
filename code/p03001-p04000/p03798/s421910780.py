import sys, os

f = lambda:list(map(int,input().split()))
if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')

def neg(i):
    if i == 'S':
        return 'W'
    else:
        return 'S'

s  = ''
n = 0

def check(build):
    poss = [0, n-1]
    for pos in poss:
        if build[pos] == 'S':
            if s[pos] == 'o' and build[(pos-1+n)%n] != build[(pos+1+n)%n]:
                return False
            if s[pos] == 'x' and build[(pos-1+n)%n] == build[(pos+1+n)%n]:
                return False
        else:
            if s[pos] == 'o' and build[(pos-1+n)%n] == build[(pos+1+n)%n]:
                return False
            if s[pos] == 'x' and build[(pos-1+n)%n] != build[(pos+1+n)%n]:
                return False
    
    return True

def solve():
    global s, n
    n = f()[0]
    s = input()

    for i in [ 'S', 'W']:
        for j in ['S','W']:
            build = i + j
            
            for k in range(1, n-1):
                if s[k] == 'o':
                    if build[k] == 'S':
                        build += build[k-1]
                    else:
                        build += neg(build[k-1])
                else:
                    if build[k] == 'S':
                        build += neg(build[k-1])
                    else:
                        build += build[k-1]

            if check(build):
                print(build)
                return

    print(-1)


solve()
